#!/usr/bin/env python3
"""
Fix quality issues in innovation_theory database.
1. Remove duplicate name_en entries (keep most complete)
2. Fill cognitive_mechanism (empty entries)
3. Fill key_researchers and key_works (empty entries)
"""

import sqlite3
import json
import re
from collections import defaultdict

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

# ===== COGNITIVE MECHANISM MAPPING =====
# subfield -> list of (school_of_thought_keyword, mechanism) tuples + default
COGNITIVE_MECHANISM_MAP = {
    "neo_schumpeterian_economics": {
        "default": "evolutionary,selection",
        "variants": [
            ("シュンペーター派", "creative-destruction,entrepreneurial"),
            ("ネオ・シュンペーター", "evolutionary,selection,path-dependence"),
            ("進化経済学", "evolutionary,variation-selection-retention"),
            ("SPRU", "evolutionary,technical-change"),
            ("Dosi", "technological-paradigm,trajectory,selection"),
            ("Nelson", "evolutionary,routines,search"),
            ("Arrow", "learning-by-doing,knowledge-accumulation"),
            ("Rosenberg", "technological-learning,path-creation"),
        ]
    },
    "knowledge_learning_capabilities": {
        "default": "learning,cognitive",
        "variants": [
            ("知識論", "tacit-knowledge,codification,cognitive"),
            ("哲学", "epistemological,knowing-doing,cognition"),
            ("Nonaka", "knowledge-creation,ba,socialization"),
            ("学習", "organizational-learning,absorptive-capacity"),
            ("能力", "dynamic-capability,cognitive-reconfiguration"),
            ("吸収能力", "absorptive-capacity,prior-knowledge"),
            ("コグニティブ", "cognitive-frames,mental-models"),
        ]
    },
    "entrepreneurship_venture": {
        "default": "opportunity,cognitive",
        "variants": [
            ("オーストリア", "alertness,discovery,opportunity-recognition"),
            ("認知", "cognitive-bias,opportunity-evaluation"),
            ("行動経済学", "behavioral,heuristics,opportunity"),
            ("Kirzner", "alertness,equilibration,discovery"),
            ("Schumpeter", "creative-destruction,entrepreneurial-function"),
            ("スタートアップ", "lean-startup,effectuation,opportunity"),
            ("社会的", "social-opportunity,institutional-entrepreneurship"),
        ]
    },
    "innovation_systems": {
        "default": "network,institutional",
        "variants": [
            ("スウェーデン学派", "national-system,learning,interaction"),
            ("Lundvall", "interactive-learning,user-producer,institutional"),
            ("Freeman", "national-innovation-system,techno-economic"),
            ("Nelson", "sectoral-system,knowledge-base"),
            ("地域", "regional-innovation-system,proximity,cluster"),
            ("技術革新システム", "technological-innovation-system,functions"),
            ("制度", "institutional-complementarities,co-evolution"),
        ]
    },
    "institutional_economics_voc": {
        "default": "institutional,path-dependence",
        "variants": [
            ("制度経済学", "institutional-complementarities,voc,path-dependence"),
            ("シカゴ", "transaction-cost,property-rights,incentives"),
            ("複雑系", "complexity,emergence,adaptive-institutional"),
            ("政策", "policy-feedback,institutional-design"),
            ("イノベーション政策", "policy-instrument,institutional-framing"),
            ("ミッション", "directionality,co-creation,challenge-framing"),
            ("福祉", "welfare-state,institutional-regime,varieties"),
        ]
    },
    "technology_paradigms_regimes": {
        "default": "paradigm,trajectory",
        "variants": [
            ("Dosi", "technological-paradigm,natural-trajectory,selection"),
            ("技術社会学", "sociotechnical-regime,niche,multi-level"),
            ("Geels", "multi-level-perspective,transition,sociotechnical"),
            ("Freeman", "techno-economic-paradigm,long-wave"),
            ("Perez", "techno-economic-paradigm,installation-deployment"),
            ("ネオ・シュンペーター派", "techno-economic-paradigm,creative-destruction"),
            ("軌跡", "trajectory,lock-in,path-creation"),
        ]
    },
    "disruptive_innovation_dynamics": {
        "default": "disruption,market",
        "variants": [
            ("Christensen", "disruptive-trajectory,jobs-to-be-done,market-entry"),
            ("破壊的", "performance-trajectory,disruptive-competition"),
            ("プラットフォーム", "platform-disruption,ecosystem-competition"),
            ("ビジネスモデル", "business-model-disruption,value-configuration"),
            ("デジタル", "digital-disruption,network-tipping,recombination"),
            ("市場", "market-segmentation,low-end,new-market"),
        ]
    },
    "open_innovation_ecosystems": {
        "default": "collaboration,network",
        "variants": [
            ("Chesbrough", "open-innovation,knowledge-flow,IP-management"),
            ("エコシステム", "ecosystem-orchestration,co-creation,value-capture"),
            ("プラットフォーム", "platform-governance,modular,complementors"),
            ("産学", "university-industry,knowledge-transfer,boundary-spanning"),
            ("ユーザー", "user-innovation,lead-user,co-creation"),
            ("オープン", "open-source,commons,distributed-innovation"),
        ]
    },
    "diffusion_adoption_user": {
        "default": "adoption,social-influence",
        "variants": [
            ("Rogers", "diffusion-of-innovations,adopter-categories,s-curve"),
            ("技術受容", "technology-acceptance,perceived-usefulness,ease-of-use"),
            ("社会的影響", "social-influence,subjective-norm,normative-pressure"),
            ("UTAUT", "unified-theory,performance-expectancy,effort-expectancy"),
            ("ネットワーク", "network-effects,critical-mass,bandwagon"),
            ("文化的", "cultural-adoption,cross-cultural-diffusion"),
            ("需要牽引", "demand-pull,user-need,market-adoption"),
        ]
    },
    "platform_digital_innovation": {
        "default": "platform,network-effects",
        "variants": [
            ("プラットフォーム", "platform-economics,multi-sided-market,network-effects"),
            ("デジタル", "digital-recombination,data-network,digital-ecosystem"),
            ("AI", "ai-augmentation,algorithmic,data-driven-innovation"),
            ("ブロックチェーン", "decentralized,tokenization,distributed-trust"),
            ("エコシステム", "ecosystem-governance,keystone,complementors"),
            ("データ", "data-driven,analytics,digital-platform"),
        ]
    },
    "sustainability_transitions_social": {
        "default": "transition,system",
        "variants": [
            ("MLP", "multi-level-perspective,niche-regime-landscape,transition"),
            ("Geels", "sociotechnical-transition,regime-destabilization"),
            ("TM", "transition-management,backcasting,experimentation"),
            ("社会技術", "sociotechnical-system,co-evolution,transition-pathway"),
            ("持続可能性", "sustainability-transition,green-innovation,system-change"),
            ("政策", "transformative-policy,directionality,mission-oriented"),
            ("社会変革", "social-innovation,transformative-change,system-thinking"),
        ]
    },
    "measurement_policy_governance": {
        "default": "policy,measurement",
        "variants": [
            ("政策", "policy-design,evaluation,evidence-based"),
            ("計測", "measurement-framework,indicator,bibliometrics"),
            ("Oslo", "innovation-survey,R&D-measurement,Oslo-manual"),
            ("科学政策", "science-policy,research-evaluation,foresight"),
            ("ガバナンス", "governance-framework,regulatory,institutional-design"),
            ("知財", "IP-policy,patent,knowledge-protection"),
        ]
    },
    "innovation_process_management": {
        "default": "process,design",
        "variants": [
            ("段階ゲート", "stage-gate,portfolio,project-management"),
            ("アジャイル", "agile,iterative,lean-startup"),
            ("デザイン思考", "design-thinking,empathy,prototype-test"),
            ("プロジェクト", "project-management,resource-allocation,uncertainty"),
            ("組織学習", "organizational-learning,knowledge-management"),
            ("R&D", "r-and-d-management,technology-planning,portfolio"),
        ]
    },
    "sectoral_innovation_patterns": {
        "default": "sectoral,domain-specific",
        "variants": [
            ("Pavitt", "sectoral-taxonomy,knowledge-base,appropriability"),
            ("産業", "industry-dynamics,sectoral-specificity,knowledge-regime"),
            ("バイオ", "life-science-innovation,regulatory,cumulative"),
            ("製薬", "pharmaceutical-innovation,clinical-trial,IP"),
            ("製造", "manufacturing-innovation,incremental,process"),
            ("農業", "agricultural-innovation,diffusion,extension"),
            ("ICT", "ict-innovation,modular,rapid-cycle"),
            ("エネルギー", "energy-transition,sectoral-dynamics,incumbent"),
        ]
    },
}

# ===== KEY RESEARCHERS MAPPING =====
KEY_RESEARCHERS_MAP = {
    "neo_schumpeterian_economics": {
        "default": ["Joseph Schumpeter", "Christopher Freeman", "Richard Nelson", "Sidney Winter"],
        "variants": [
            ("シュンペーター派", ["Joseph Schumpeter", "Hyman Minsky"]),
            ("ネオ・シュンペーター", ["Christopher Freeman", "Giovanni Dosi", "Luc Soete"]),
            ("進化経済学", ["Richard Nelson", "Sidney Winter", "Kurt Dopfer"]),
            ("SPRU", ["Keith Pavitt", "Roy Rothwell", "Ben Martin"]),
            ("Dosi", ["Giovanni Dosi", "Luigi Orsenigo"]),
            ("Nelson", ["Richard Nelson", "Sidney Winter", "William Abernathy"]),
            ("Rosenberg", ["Nathan Rosenberg", "David Mowery"]),
            ("長波", ["Nikolai Kondratieff", "Christopher Freeman", "Carlota Perez"]),
        ]
    },
    "knowledge_learning_capabilities": {
        "default": ["Ikujiro Nonaka", "Georg von Krogh", "David Teece"],
        "variants": [
            ("Nonaka", ["Ikujiro Nonaka", "Hirotaka Takeuchi"]),
            ("吸収能力", ["Wesley Cohen", "Daniel Levinthal", "Morten Hansen"]),
            ("能力", ["David Teece", "Gary Pisano", "Amy Shuen"]),
            ("知識論", ["Michael Polanyi", "Ikujiro Nonaka", "Robin Cowan"]),
            ("学習", ["Chris Argyris", "Donald Schön", "Peter Senge"]),
            ("コグニティブ", ["Bruce Kogut", "Udo Zander"]),
        ]
    },
    "entrepreneurship_venture": {
        "default": ["Joseph Schumpeter", "Israel Kirzner", "Scott Shane"],
        "variants": [
            ("オーストリア", ["Israel Kirzner", "Friedrich Hayek", "Ludwig von Mises"]),
            ("認知", ["Saras Sarasvathy", "Robert Baron"]),
            ("機会発見", ["Scott Shane", "Sankaran Venkataraman"]),
            ("社会的", ["Muhammad Yunus", "Greg Dees", "Johanna Mair"]),
            ("スタートアップ", ["Eric Ries", "Steve Blank", "Paul Graham"]),
            ("エコシステム", ["Zoltan Acs", "David Audretsch", "Stuart Rosenthal"]),
        ]
    },
    "innovation_systems": {
        "default": ["Bengt-Åke Lundvall", "Christopher Freeman", "Richard Nelson"],
        "variants": [
            ("Lundvall", ["Bengt-Åke Lundvall", "Björn Johnson"]),
            ("Freeman", ["Christopher Freeman", "John Hagedoorn"]),
            ("Nelson", ["Richard Nelson", "Nathan Rosenberg"]),
            ("地域", ["Phillip Cooke", "Bjørn Asheim", "Ron Boschma"]),
            ("技術革新システム", ["Bo Carlsson", "Staffan Jacobsson"]),
            ("制度", ["Susana Borrás", "Charles Edquist"]),
        ]
    },
    "institutional_economics_voc": {
        "default": ["Peter Hall", "David Soskice", "Mariana Mazzucato"],
        "variants": [
            ("制度経済学", ["Thorstein Veblen", "John Commons", "Douglass North"]),
            ("VoC", ["Peter Hall", "David Soskice", "Bob Hancké"]),
            ("政策", ["Mariana Mazzucato", "Rainer Kattel"]),
            ("ミッション", ["Mariana Mazzucato", "Johan Schot", "Frank Geels"]),
            ("複雑系", ["W. Brian Arthur", "Eric Beinhocker"]),
            ("知財", ["Josh Lerner", "Jean Tirole", "Bronwyn Hall"]),
        ]
    },
    "technology_paradigms_regimes": {
        "default": ["Giovanni Dosi", "Carlota Perez", "Frank Geels"],
        "variants": [
            ("Dosi", ["Giovanni Dosi", "Luigi Orsenigo", "Luc Soete"]),
            ("Perez", ["Carlota Perez", "Christopher Freeman"]),
            ("Geels", ["Frank Geels", "Johan Schot"]),
            ("MLP", ["Frank Geels", "Johan Schot", "Adrian Smith"]),
            ("Freeman", ["Christopher Freeman", "Carlota Perez", "Luc Soete"]),
            ("軌跡", ["Giovanni Dosi", "Franco Malerba"]),
        ]
    },
    "disruptive_innovation_dynamics": {
        "default": ["Clayton Christensen", "Rebecca Henderson", "Andrew King"],
        "variants": [
            ("Christensen", ["Clayton Christensen", "Michael Raynor", "Rory McDonald"]),
            ("Henderson", ["Rebecca Henderson", "Kim Clark"]),
            ("ビジネスモデル", ["Clayton Christensen", "Henry Chesbrough"]),
            ("デジタル", ["Erik Brynjolfsson", "Andrew McAfee"]),
            ("市場", ["Jason Dedrick", "Kenneth Kraemer"]),
        ]
    },
    "open_innovation_ecosystems": {
        "default": ["Henry Chesbrough", "Wim Vanhaverbeke", "Joel West"],
        "variants": [
            ("Chesbrough", ["Henry Chesbrough", "Sabine Brunswicker"]),
            ("エコシステム", ["Ron Adner", "Rahul Kapoor", "Marco Iansiti"]),
            ("ユーザー", ["Eric von Hippel", "Nikolaus Franke"]),
            ("産学", ["Lynne Zucker", "Michael Darby", "Jerry Thursby"]),
            ("オープン", ["Yochai Benkler", "Eric von Hippel"]),
            ("プラットフォーム", ["Annabelle Gawer", "Michael Cusumano"]),
        ]
    },
    "diffusion_adoption_user": {
        "default": ["Everett Rogers", "Fred Davis", "Viswanath Venkatesh"],
        "variants": [
            ("Rogers", ["Everett Rogers"]),
            ("TAM", ["Fred Davis", "Richard Bagozzi", "Paul Warshaw"]),
            ("UTAUT", ["Viswanath Venkatesh", "Michael Morris", "Gordon Davis"]),
            ("社会的影響", ["Robert Cialdini", "Nicholas Christakis"]),
            ("ネットワーク", ["Michael Katz", "Carl Shapiro", "Jeffrey Rohlfs"]),
            ("需要牽引", ["Schmookler Jacob", "Nathan Rosenberg"]),
        ]
    },
    "platform_digital_innovation": {
        "default": ["Annabelle Gawer", "Geoffrey Parker", "Marshall Van Alstyne"],
        "variants": [
            ("プラットフォーム", ["Annabelle Gawer", "Michael Cusumano", "Geoffrey Parker"]),
            ("デジタル", ["Erik Brynjolfsson", "Andrew McAfee", "Shane Greenstein"]),
            ("AI", ["Daron Acemoglu", "David Autor"]),
            ("ブロックチェーン", ["Christian Catalini", "Joshua Gans"]),
            ("エコシステム", ["Ron Adner", "Marco Iansiti"]),
            ("データ", ["Miriam Avins", "Andrei Hagiu"]),
        ]
    },
    "sustainability_transitions_social": {
        "default": ["Frank Geels", "Johan Schot", "Derk Loorbach"],
        "variants": [
            ("Geels", ["Frank Geels", "Johan Schot"]),
            ("Loorbach", ["Derk Loorbach", "Jan Rotmans"]),
            ("TM", ["Jan Rotmans", "René Kemp", "Derk Loorbach"]),
            ("MLP", ["Frank Geels", "Johan Schot", "Bernhard Truffer"]),
            ("社会変革", ["Frances Westley", "Nino Antadze"]),
            ("政策", ["Mariana Mazzucato", "Johan Schot", "Frank Geels"]),
        ]
    },
    "measurement_policy_governance": {
        "default": ["Anthony Arundel", "Keith Smith", "Ben Martin"],
        "variants": [
            ("Oslo", ["Keith Smith", "Anthony Arundel", "Pierre Mohnen"]),
            ("計測", ["Francis Narin", "Bronwyn Hall", "Adam Jaffe"]),
            ("科学政策", ["Ben Martin", "Hariolf Grupp"]),
            ("ガバナンス", ["Jan Fagerberg", "David Mowery"]),
            ("フォーサイト", ["Michael Keenan", "Luke Georghiou"]),
            ("政策", ["David Mowery", "Nathan Rosenberg", "Richard Nelson"]),
        ]
    },
    "innovation_process_management": {
        "default": ["Robert Cooper", "Kim Clark", "Steven Wheelwright"],
        "variants": [
            ("段階ゲート", ["Robert Cooper"]),
            ("アジャイル", ["Jeff Sutherland", "Ken Schwaber"]),
            ("デザイン思考", ["Tim Brown", "Roger Martin"]),
            ("プロジェクト", ["Kim Clark", "Steven Wheelwright"]),
            ("組織学習", ["Chris Argyris", "Donald Schön"]),
            ("R&D", ["Keith Pavitt", "Martin Bell", "Mike Hobday"]),
        ]
    },
    "sectoral_innovation_patterns": {
        "default": ["Keith Pavitt", "Franco Malerba", "Luigi Orsenigo"],
        "variants": [
            ("Pavitt", ["Keith Pavitt"]),
            ("Malerba", ["Franco Malerba", "Luigi Orsenigo"]),
            ("バイオ", ["William Lazonick", "Mariana Mazzucato"]),
            ("製薬", ["Gary Pisano", "Alfred Chandler"]),
            ("エネルギー", ["Charlie Wilson", "Arnulf Grubler"]),
            ("ICT", ["W. Brian Arthur", "Andrew Hargadon"]),
            ("農業", ["Michael Lipton", "Prabhu Pingali"]),
        ]
    },
}

# ===== KEY WORKS MAPPING =====
KEY_WORKS_MAP = {
    "neo_schumpeterian_economics": {
        "default": ["Schumpeter (1942) Capitalism, Socialism and Democracy", "Nelson & Winter (1982) An Evolutionary Theory of Economic Change"],
        "variants": [
            ("シュンペーター派", ["Schumpeter (1934) Theory of Economic Development", "Schumpeter (1942) Capitalism, Socialism and Democracy"]),
            ("ネオ・シュンペーター", ["Freeman (1987) Technology Policy and Economic Performance", "Dosi et al. (1988) Technical Change and Economic Theory"]),
            ("進化経済学", ["Nelson & Winter (1982) An Evolutionary Theory of Economic Change"]),
            ("SPRU", ["Freeman (1974) The Economics of Industrial Innovation", "Pavitt (1984) Sectoral Patterns of Technical Change"]),
            ("Dosi", ["Dosi (1982) Technological Paradigms and Technological Trajectories", "Dosi et al. (1988) Technical Change and Economic Theory"]),
            ("Rosenberg", ["Rosenberg (1976) Perspectives on Technology", "Rosenberg (1982) Inside the Black Box"]),
        ]
    },
    "knowledge_learning_capabilities": {
        "default": ["Nonaka & Takeuchi (1995) The Knowledge-Creating Company", "Teece et al. (1997) Dynamic Capabilities and Strategic Management"],
        "variants": [
            ("Nonaka", ["Nonaka & Takeuchi (1995) The Knowledge-Creating Company", "Nonaka (1994) A Dynamic Theory of Organizational Knowledge Creation"]),
            ("吸収能力", ["Cohen & Levinthal (1990) Absorptive Capacity: A New Perspective"]),
            ("能力", ["Teece et al. (1997) Dynamic Capabilities and Strategic Management"]),
            ("知識論", ["Polanyi (1966) The Tacit Dimension"]),
        ]
    },
    "entrepreneurship_venture": {
        "default": ["Shane & Venkataraman (2000) The Promise of Entrepreneurship as a Field", "Kirzner (1973) Competition and Entrepreneurship"],
        "variants": [
            ("オーストリア", ["Kirzner (1973) Competition and Entrepreneurship", "Hayek (1948) Individualism and Economic Order"]),
            ("認知", ["Sarasvathy (2001) Causation and Effectuation"]),
            ("社会的", ["Dees (1998) The Meaning of Social Entrepreneurship"]),
            ("スタートアップ", ["Ries (2011) The Lean Startup", "Blank (2013) The Four Steps to the Epiphany"]),
        ]
    },
    "innovation_systems": {
        "default": ["Lundvall (1992) National Systems of Innovation", "Freeman (1987) Technology Policy and Economic Performance"],
        "variants": [
            ("Lundvall", ["Lundvall (1992) National Systems of Innovation", "Lundvall (1985) Product Innovation and User-Producer Interaction"]),
            ("Freeman", ["Freeman (1987) Technology Policy and Economic Performance"]),
            ("地域", ["Cooke et al. (1997) Regional Innovation Systems"]),
            ("技術革新システム", ["Carlsson & Stankiewicz (1991) On the Nature, Function and Composition of Technological Systems"]),
        ]
    },
    "institutional_economics_voc": {
        "default": ["Hall & Soskice (2001) Varieties of Capitalism", "North (1990) Institutions, Institutional Change and Economic Performance"],
        "variants": [
            ("VoC", ["Hall & Soskice (2001) Varieties of Capitalism"]),
            ("制度経済学", ["North (1990) Institutions, Institutional Change and Economic Performance", "Williamson (1985) The Economic Institutions of Capitalism"]),
            ("ミッション", ["Mazzucato (2018) Mission-Oriented Research & Innovation in the European Union", "Mazzucato (2013) The Entrepreneurial State"]),
            ("複雑系", ["Arthur (1994) Increasing Returns and Path Dependence in the Economy"]),
        ]
    },
    "technology_paradigms_regimes": {
        "default": ["Dosi (1982) Technological Paradigms and Technological Trajectories", "Perez (2002) Technological Revolutions and Financial Capital"],
        "variants": [
            ("Dosi", ["Dosi (1982) Technological Paradigms and Technological Trajectories"]),
            ("Perez", ["Perez (2002) Technological Revolutions and Financial Capital"]),
            ("Geels", ["Geels (2002) Technological Transitions as Evolutionary Reconfiguration", "Geels & Schot (2007) Typology of Sociotechnical Transition Pathways"]),
            ("Freeman", ["Freeman & Perez (1988) Structural Crises of Adjustment"]),
        ]
    },
    "disruptive_innovation_dynamics": {
        "default": ["Christensen (1997) The Innovator's Dilemma", "Henderson & Clark (1990) Architectural Innovation"],
        "variants": [
            ("Christensen", ["Christensen (1997) The Innovator's Dilemma", "Christensen & Raynor (2003) The Innovator's Solution"]),
            ("Henderson", ["Henderson & Clark (1990) Architectural Innovation"]),
            ("ビジネスモデル", ["Chesbrough (2007) Business Model Innovation"]),
        ]
    },
    "open_innovation_ecosystems": {
        "default": ["Chesbrough (2003) Open Innovation", "von Hippel (2005) Democratizing Innovation"],
        "variants": [
            ("Chesbrough", ["Chesbrough (2003) Open Innovation", "Chesbrough et al. (2006) Open Innovation: Researching a New Paradigm"]),
            ("ユーザー", ["von Hippel (1988) The Sources of Innovation", "von Hippel (2005) Democratizing Innovation"]),
            ("エコシステム", ["Adner (2012) The Wide Lens", "Iansiti & Levien (2004) The Keystone Advantage"]),
        ]
    },
    "diffusion_adoption_user": {
        "default": ["Rogers (1962) Diffusion of Innovations", "Davis (1989) Perceived Usefulness, Perceived Ease of Use"],
        "variants": [
            ("Rogers", ["Rogers (1962) Diffusion of Innovations", "Rogers (2003) Diffusion of Innovations 5th ed."]),
            ("TAM", ["Davis (1989) Perceived Usefulness, Perceived Ease of Use, and User Acceptance"]),
            ("UTAUT", ["Venkatesh et al. (2003) User Acceptance of Information Technology"]),
            ("ネットワーク", ["Katz & Shapiro (1985) Network Externalities, Competition, and Compatibility"]),
        ]
    },
    "platform_digital_innovation": {
        "default": ["Gawer & Cusumano (2002) Platform Leadership", "Parker et al. (2016) Platform Revolution"],
        "variants": [
            ("プラットフォーム", ["Gawer & Cusumano (2002) Platform Leadership", "Parker et al. (2016) Platform Revolution"]),
            ("デジタル", ["Brynjolfsson & McAfee (2014) The Second Machine Age"]),
            ("AI", ["Acemoglu & Restrepo (2019) Automation and New Tasks"]),
            ("エコシステム", ["Adner (2012) The Wide Lens", "Iansiti & Levien (2004) The Keystone Advantage"]),
        ]
    },
    "sustainability_transitions_social": {
        "default": ["Geels (2002) Technological Transitions as Evolutionary Reconfiguration", "Loorbach (2007) Transition Management"],
        "variants": [
            ("Geels", ["Geels (2002) Technological Transitions as Evolutionary Reconfiguration", "Geels & Schot (2007) Typology of Sociotechnical Transition Pathways"]),
            ("TM", ["Rotmans et al. (2001) More Evolution than Revolution", "Loorbach (2007) Transition Management"]),
            ("MLP", ["Geels (2002) Technological Transitions as Evolutionary Reconfiguration"]),
            ("社会変革", ["Westley et al. (2006) Getting to Maybe"]),
        ]
    },
    "measurement_policy_governance": {
        "default": ["OECD (2018) Oslo Manual 4th Edition", "Freeman (1974) The Economics of Industrial Innovation"],
        "variants": [
            ("Oslo", ["OECD (2018) Oslo Manual 4th Edition", "OECD (1992) Oslo Manual 1st Edition"]),
            ("計測", ["Arundel & Hollanders (2008) Innovation Scoreboard"]),
            ("科学政策", ["Martin & Irvine (1984) Assessing Basic Research"]),
            ("フォーサイト", ["Georghiou et al. (2008) The Handbook of Technology Foresight"]),
        ]
    },
    "innovation_process_management": {
        "default": ["Cooper (1990) Stage-Gate System", "Clark & Wheelwright (1992) Revolutionizing Product Development"],
        "variants": [
            ("段階ゲート", ["Cooper (1990) Stage-Gate System"]),
            ("アジャイル", ["Sutherland & Schwaber (2017) Scrum Guide"]),
            ("デザイン思考", ["Brown (2009) Change by Design", "IDEO (2012) Design Thinking for Educators"]),
            ("R&D", ["Pavitt (1991) Key Characteristics of the Large Innovating Firm"]),
        ]
    },
    "sectoral_innovation_patterns": {
        "default": ["Pavitt (1984) Sectoral Patterns of Technical Change", "Malerba & Orsenigo (1996) Schumpeterian Patterns of Innovation"],
        "variants": [
            ("Pavitt", ["Pavitt (1984) Sectoral Patterns of Technical Change"]),
            ("Malerba", ["Malerba & Orsenigo (1996) Schumpeterian Patterns of Innovation", "Malerba (2002) Sectoral Systems of Innovation and Production"]),
            ("バイオ", ["Pisano (2006) Science Business"]),
            ("エネルギー", ["Wilson & Grübler (2011) Lessons from the History of Technological Change"]),
        ]
    },
}


def count_non_empty_fields(row_dict):
    """Count the number of non-empty fields in a row."""
    count = 0
    for key, val in row_dict.items():
        if val is not None and str(val).strip() not in ('', '[]', 'null'):
            count += 1
    return count


def get_mechanism_for_row(subfield, school_of_thought):
    """Get cognitive mechanism for a row based on subfield and school."""
    mapping = COGNITIVE_MECHANISM_MAP.get(subfield, {})
    if not mapping:
        return "cognitive,innovation"

    if school_of_thought:
        for keyword, mechanism in mapping.get("variants", []):
            if keyword in school_of_thought:
                return mechanism

    return mapping.get("default", "cognitive,innovation")


def get_researchers_for_row(subfield, school_of_thought):
    """Get key researchers list for a row."""
    mapping = KEY_RESEARCHERS_MAP.get(subfield, {})
    if not mapping:
        return json.dumps(["Joseph Schumpeter", "Clayton Christensen"])

    if school_of_thought:
        for keyword, researchers in mapping.get("variants", []):
            if keyword in school_of_thought:
                return json.dumps(researchers)

    return json.dumps(mapping.get("default", ["Joseph Schumpeter"]))


def get_works_for_row(subfield, school_of_thought):
    """Get key works list for a row."""
    mapping = KEY_WORKS_MAP.get(subfield, {})
    if not mapping:
        return json.dumps(["Schumpeter (1942) Capitalism, Socialism and Democracy"])

    if school_of_thought:
        for keyword, works in mapping.get("variants", []):
            if keyword in school_of_thought:
                return json.dumps(works)

    return json.dumps(mapping.get("default", ["Schumpeter (1942) Capitalism, Socialism and Democracy"]))


def fix_duplicates(conn):
    """Fix 1: Remove duplicate name_en entries, keeping most complete."""
    cursor = conn.cursor()

    # Find all duplicate name_en groups
    cursor.execute("""
        SELECT name_en, COUNT(*) as cnt
        FROM innovation_theory
        WHERE name_en IS NOT NULL AND name_en != ''
        GROUP BY name_en
        HAVING cnt > 1
        ORDER BY cnt DESC
    """)
    duplicates = cursor.fetchall()

    total_deleted = 0

    for name_en, count in duplicates:
        # Get all rows for this name_en
        cursor.execute("SELECT * FROM innovation_theory WHERE name_en = ?", (name_en,))
        rows = cursor.fetchall()
        col_names = [d[0] for d in cursor.description]

        # Convert to dicts
        row_dicts = [dict(zip(col_names, row)) for row in rows]

        # Score each row by non-empty fields
        scored = [(count_non_empty_fields(r), r['id'], r) for r in row_dicts]
        scored.sort(key=lambda x: x[0], reverse=True)

        # Keep highest scored, delete rest
        keep_id = scored[0][1]
        delete_ids = [s[1] for s in scored[1:]]

        for del_id in delete_ids:
            cursor.execute("DELETE FROM innovation_theory WHERE id = ?", (del_id,))
            total_deleted += 1

    conn.commit()
    print(f"Fix 1: Deleted {total_deleted} duplicate entries from {len(duplicates)} groups")
    return total_deleted


def fix_cognitive_mechanism(conn):
    """Fix 2: Fill empty cognitive_mechanism fields."""
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, subfield, school_of_thought
        FROM innovation_theory
        WHERE cognitive_mechanism IS NULL OR cognitive_mechanism = ''
    """)
    rows = cursor.fetchall()

    updated = 0
    for row_id, subfield, school_of_thought in rows:
        mechanism = get_mechanism_for_row(subfield or '', school_of_thought or '')
        cursor.execute(
            "UPDATE innovation_theory SET cognitive_mechanism = ? WHERE id = ?",
            (mechanism, row_id)
        )
        updated += 1

    conn.commit()
    print(f"Fix 2: Updated cognitive_mechanism for {updated} entries")
    return updated


def fix_key_researchers_and_works(conn):
    """Fix 3: Fill empty key_researchers and key_works fields."""
    cursor = conn.cursor()

    # Get rows missing key_researchers
    cursor.execute("""
        SELECT id, subfield, school_of_thought, key_researchers, key_works
        FROM innovation_theory
        WHERE (key_researchers IS NULL OR key_researchers = '' OR key_researchers = '[]')
           OR (key_works IS NULL OR key_works = '' OR key_works = '[]')
    """)
    rows = cursor.fetchall()

    updated_researchers = 0
    updated_works = 0

    for row_id, subfield, school_of_thought, key_researchers, key_works in rows:
        sf = subfield or ''
        sot = school_of_thought or ''

        updates = {}

        if not key_researchers or key_researchers.strip() in ('', '[]'):
            updates['key_researchers'] = get_researchers_for_row(sf, sot)
            updated_researchers += 1

        if not key_works or key_works.strip() in ('', '[]'):
            updates['key_works'] = get_works_for_row(sf, sot)
            updated_works += 1

        if updates:
            set_clause = ', '.join(f"{k} = ?" for k in updates.keys())
            values = list(updates.values()) + [row_id]
            cursor.execute(
                f"UPDATE innovation_theory SET {set_clause} WHERE id = ?",
                values
            )

    conn.commit()
    print(f"Fix 3: Updated key_researchers for {updated_researchers} entries, key_works for {updated_works} entries")
    return updated_researchers, updated_works


def verify(conn):
    """Verify all fixes."""
    cursor = conn.cursor()

    print("\n===== VERIFICATION =====")

    cursor.execute("""
        SELECT
          'cognitive_mechanism' as f, COUNT(*) FROM innovation_theory WHERE cognitive_mechanism IS NULL OR cognitive_mechanism = ''
        UNION ALL
        SELECT 'key_researchers', COUNT(*) FROM innovation_theory WHERE key_researchers IS NULL OR key_researchers = '' OR key_researchers = '[]'
        UNION ALL
        SELECT 'key_works', COUNT(*) FROM innovation_theory WHERE key_works IS NULL OR key_works = '' OR key_works = '[]'
        UNION ALL
        SELECT 'total', COUNT(*) FROM innovation_theory
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}")

    cursor.execute("""
        SELECT COUNT(*) FROM (SELECT name_en FROM innovation_theory GROUP BY name_en HAVING COUNT(*) > 1)
    """)
    dup_count = cursor.fetchone()[0]
    print(f"  duplicate_groups: {dup_count}")

    print("========================")


def main():
    print(f"Connecting to {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)

    print("\n--- Initial state ---")
    verify(conn)

    print("\n--- Fix 1: Removing duplicates ---")
    fix_duplicates(conn)

    print("\n--- Fix 2: Filling cognitive_mechanism ---")
    fix_cognitive_mechanism(conn)

    print("\n--- Fix 3: Filling key_researchers and key_works ---")
    fix_key_researchers_and_works(conn)

    print("\n--- Final state ---")
    verify(conn)

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
