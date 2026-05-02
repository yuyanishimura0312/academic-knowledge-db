#!/usr/bin/env python3
"""
Build cross_domain_relations connecting innovation_theory to all other domain tables.
Target: 500+ relations. Optimised for performance with batch inserts.
"""

import sqlite3
import uuid
from datetime import datetime, timezone

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def make_id():
    return "inno_" + str(uuid.uuid4())[:8]

def now_str():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

# ─────────────────────────────────────────────────────────────────────────────
# CURATED relations: (inno_name_frag, target_table, target_name_frag,
#                    relation_type, description, strength)
# ─────────────────────────────────────────────────────────────────────────────
CURATED = [
    # ── innovation_theory ↔ social_theory ─────────────────────────────────
    ("Creative Destruction", "social_theory", "New Institutionalism",
     "theoretical_parallel", "Both address displacement of incumbents—Schumpeter via economic dynamics, New Institutionalism via legitimacy shifts.", 8),
    ("Creative Destruction", "social_theory", "Deinstitutionalization",
     "conceptual_parallel", "Deinstitutionalization is the sociological counterpart to creative destruction: old institutional logics erode as new ones emerge.", 9),
    ("National Innovation System", "social_theory", "Organizational Field",
     "conceptual_parallel", "National Innovation Systems and organizational fields both describe bounded arenas where actors co-evolve under shared norms.", 8),
    ("Triple Helix", "social_theory", "Organizational Field",
     "applied_to", "Triple Helix analyses the university–industry–government field as an organizational field with distinct institutional logics.", 7),
    ("Institutional Entrepreneur", "social_theory", "Institutional Entrepreneur",
     "conceptual_parallel", "Innovation-driven and sociological institutional entrepreneurship both frame actors who disrupt existing orders by creating new rules.", 10),
    ("Absorptive Capacity", "social_theory", "Social Capital",
     "conceptual_parallel", "Absorptive capacity at firm level mirrors social capital at network level: both explain differential access to external knowledge.", 8),
    ("Open Innovation", "social_theory", "Social Capital",
     "applied_to", "Open innovation networks depend on bridging social capital to connect diverse knowledge pools across organisational boundaries.", 8),
    ("Knowledge Spillover", "social_theory", "Social Network Analysis",
     "operationalizes", "SNA operationalises knowledge spillover theory by mapping structural conduits through which knowledge diffuses.", 9),
    ("Diffusion of Innovations", "social_theory", "Social Network Analysis",
     "applied_to", "Rogers' diffusion model relies on network ties as conduits; SNA provides the analytical toolkit to map adoption curves.", 9),
    ("Path Dependence", "social_theory", "Historical Institutionalism",
     "theoretical_foundation", "Historical institutionalism formalises path dependence: critical junctures shape subsequent innovation trajectories.", 9),
    ("Technological Paradigm", "social_theory", "Paradigm Shift",
     "conceptual_parallel", "Dosi's technological paradigms mirror Kuhn's paradigms adopted by social theorists: both describe punctuated equilibria.", 9),
    ("Entrepreneurship Theory", "social_theory", "Institutional Entrepreneur",
     "theoretical_foundation", "Schumpeterian entrepreneurship and sociological institutional entrepreneurship both frame actors who disrupt existing orders.", 9),
    ("Design Thinking", "social_theory", "Phenomenology",
     "philosophical_foundation", "Design thinking's empathy phase draws on phenomenological methods—understanding user experience as lived, embodied phenomena.", 8),
    ("Frugal Innovation", "social_theory", "Capability Approach",
     "applied_to", "Frugal innovation is grounded in Sen's capability approach: innovations succeed when they expand what people can do and be.", 8),
    ("Inclusive Innovation", "social_theory", "Capability Approach",
     "theoretical_foundation", "Inclusive innovation explicitly adopts the capability approach to evaluate whether innovations expand freedoms for marginalised populations.", 9),
    ("Platform Theory", "social_theory", "Transaction Cost Economics",
     "theoretical_foundation", "Platform theory extends transaction cost economics: platforms reduce multi-sided market interaction costs by managing governance and trust.", 9),
    ("Business Model Innovation", "social_theory", "Agency Theory",
     "theoretical_foundation", "Business model innovation must solve agency problems between platform owners, complementors, and users.", 8),
    ("Innovation Policy", "social_theory", "Mechanism Design",
     "applied_to", "Optimal innovation policy employs mechanism design principles: crafting incentive-compatible rules for R&D subsidies and patent systems.", 9),
    ("R&D Alliance", "social_theory", "Game Theory",
     "applied_to", "R&D alliances are modelled as games: partners choose knowledge-sharing levels considering hold-up and free-rider risks.", 8),
    ("Technology Transfer", "social_theory", "Social Network Analysis",
     "operationalizes", "SNA maps interpersonal and inter-organisational ties that carry technology transfer across institutional boundaries.", 8),
    ("Innovation Cluster", "social_theory", "Social Capital",
     "conceptual_parallel", "Cluster competitiveness is grounded in dense local social capital facilitating trust, knowledge sharing, and collective action.", 9),
    ("Responsible Innovation", "social_theory", "Ethical Theory",
     "normative_foundation", "Responsible innovation draws on ethical frameworks—deontological, consequentialist, virtue ethics—to articulate obligations.", 9),
    ("Social Innovation", "social_theory", "Community Psychology",
     "theoretical_foundation", "Social innovation builds on community psychology's emphasis on collective agency, local assets, and structural barriers to wellbeing.", 8),
    ("Grassroots Innovation", "social_theory", "Social Movement Theory",
     "theoretical_foundation", "Grassroots innovation shares ground with social movement theory: non-elite collectives mobilise resources to challenge incumbents.", 8),
    ("Technology Acceptance Model", "social_theory", "Attitude-Behavior Theory",
     "theoretical_foundation", "TAM derives from Theory of Reasoned Action: perceived usefulness and ease-of-use are attitude constructs predicting adoption.", 9),
    ("Coevolution", "social_theory", "Evolutionary Economics",
     "theoretical_foundation", "Coevolution in innovation draws on evolutionary economics: firms, technologies, and institutions co-adapt through variation-selection-retention.", 9),
    ("Disruptive Innovation", "social_theory", "Institutional Isomorphism",
     "theoretical_parallel", "Disruptive innovation explains why isomorphic incumbent firms fail: legitimacy pressures trap them in sustaining trajectories.", 8),
    ("Responsible Research and Innovation", "social_theory", "Deliberative Democracy",
     "normative_foundation", "RRI draws on deliberative democracy: publics should participate in setting research agendas and anticipating technology impacts.", 9),
    ("Innovation Ecosystem", "social_theory", "Institutional Logics",
     "conceptual_parallel", "Innovation ecosystems embed competing institutional logics (commercial, scientific, civic) that actors must navigate to co-create value.", 8),
    ("Network Effects", "social_theory", "Social Network Analysis",
     "operationalizes", "Network effects are formalised through SNA: nodes gain utility as density increases, captured by degree and clustering metrics.", 8),
    ("Organizational Learning", "social_theory", "Communities of Practice",
     "theoretical_foundation", "Communities of Practice provide the social mechanism through which organisational learning and knowledge accumulation occur.", 9),
    ("Lean Startup", "social_theory", "Grounded Theory",
     "methodological_parallel", "Lean startup's build-measure-learn cycle parallels grounded theory's iterative abduction: both generate theory from empirical feedback.", 7),
    ("User Innovation", "social_theory", "Participatory Action Research",
     "applied_to", "User innovation taps participatory action research: users as co-designers generate knowledge through doing.", 7),
    ("Quadruple Helix", "social_theory", "Participatory Democracy",
     "theoretical_parallel", "Quadruple Helix incorporates civil society as a fourth stakeholder, echoing participatory democracy's demand for inclusive governance.", 8),
    ("Social Entrepreneurship", "social_theory", "Institutional Logics",
     "applied_to", "Social entrepreneurs navigate hybrid institutional logics (commercial vs. social-mission), blending competing logics.", 8),
    ("Patent System", "social_theory", "Incomplete Contract Theory",
     "theoretical_foundation", "Patent law is an incomplete contract: it cannot specify all applications, leaving residual rights allocation as a policy challenge.", 8),
    ("Knowledge Commons", "social_theory", "Ostrom Commons",
     "theoretical_foundation", "Innovation commons theory draws on Ostrom's commons framework to govern shared knowledge pools without privatisation.", 9),
    ("National Innovation System", "social_theory", "Institutional Isomorphism",
     "conceptual_parallel", "Within national innovation systems, institutional isomorphism drives convergence of R&D practices across firms.", 7),
    ("Sharing Economy", "social_theory", "Transaction Cost Economics",
     "applied_to", "Sharing-economy platforms dramatically lower transaction costs for temporary asset utilisation.", 8),
    ("Technological Regime", "social_theory", "Regulative, Normative & Cognitive Pillars",
     "theoretical_parallel", "Technological regimes encode regulative, normative, and cognitive pillars that constrain innovation trajectories.", 8),

    # ── innovation_theory ↔ engineering_method ────────────────────────────
    ("Minimum Viable Product", "engineering_method", "Agile Development",
     "methodological_parallel", "MVP and agile sprints share iterative build-test-learn logic, minimising waste by deferring costly feature development until demand is validated.", 9),
    ("Lean Startup", "engineering_method", "Agile Development",
     "applied_to", "Lean startup operationalises agile principles at the business-model level: customer discovery maps directly onto agile sprints.", 9),
    ("Technology Roadmap", "engineering_method", "Systems Engineering",
     "applied_to", "Technology roadmapping applies systems engineering's structured decomposition to align R&D investments with product architecture evolution.", 8),
    ("Dominant Design", "engineering_method", "Design Patterns",
     "conceptual_parallel", "Dominant design resembles canonical design patterns: both become reference architectures constraining subsequent variation.", 8),
    ("Architectural Innovation", "engineering_method", "System Architecture",
     "theoretical_foundation", "Architectural innovation directly informs systems architecture: changing component linkages redefines system performance.", 9),
    ("Modular Innovation", "engineering_method", "Modular Design",
     "theoretical_foundation", "Modular innovation underpins modular design: stable interfaces permit independent subsystem innovation.", 9),
    ("Platform Innovation", "engineering_method", "API Design",
     "applied_to", "Platform innovation strategies are implemented through deliberate API design that governs third-party complementor innovation.", 8),
    ("Open Innovation", "engineering_method", "DevOps",
     "applied_to", "Open innovation is operationalised in DevOps: CI/CD pipelines facilitate rapid external contribution and feedback.", 7),
    ("Technology S-Curve", "engineering_method", "Technology Readiness Level",
     "operationalizes", "NASA TRLs map onto S-curve phases: TRL 1-3 is basic research, TRL 4-6 is scaling, TRL 7-9 is maturity.", 9),
    ("Design Thinking", "engineering_method", "User-Centered Design",
     "theoretical_foundation", "Design thinking is the meta-framework within which UCD methods (personas, journey maps, prototyping) are applied.", 9),
    ("Frugal Innovation", "engineering_method", "Lean Manufacturing",
     "applied_to", "Frugal innovation leverages lean manufacturing's waste-elimination principles to develop low-cost products.", 8),
    ("Quality Function Deployment", "engineering_method", "Requirements Engineering",
     "applied_to", "QFD bridges innovation strategy and requirements engineering: customer voice is translated into technical specifications.", 9),
    ("Concurrent Engineering", "engineering_method", "Model-Based Systems Engineering",
     "applied_to", "Concurrent engineering leverages MBSE to enable parallel design streams maintaining system coherence through shared digital models.", 8),
    ("Stage-Gate Process", "engineering_method", "Software Development Lifecycle",
     "methodological_parallel", "Stage-gate and SDLC gating share structured go/no-go decisions, reducing risk by synchronising investment with validated progress.", 8),
    ("Digital Innovation", "engineering_method", "Cloud Computing",
     "applied_to", "Digital innovation is enabled by cloud infrastructure: elastic scalability allows rapid service scaling without capital expenditure.", 9),
    ("Industry 4.0", "engineering_method", "IoT Systems",
     "applied_to", "Industry 4.0 frameworks are implemented through IoT sensor networks, edge computing, and cyber-physical systems integration.", 9),
    ("Sustainable Innovation", "engineering_method", "Life Cycle Assessment",
     "applied_to", "Sustainable innovation mandates LCA to verify that environmental impacts are reduced across the full product value chain.", 9),
    ("Open Source Innovation", "engineering_method", "Version Control",
     "applied_to", "Open source innovation depends on distributed version control (git) that enables asynchronous, parallel global contribution.", 9),
    ("Additive Manufacturing Innovation", "engineering_method", "3D Printing",
     "applied_to", "Additive manufacturing innovation is implemented through 3D printing enabling mass customisation and distributed production.", 9),
    ("Nanotechnology Innovation", "engineering_method", "Nanofabrication",
     "applied_to", "Nanotechnology innovation is operationalised through nanofabrication methods controlling matter at atomic and molecular scales.", 9),
    ("Quantum Computing Innovation", "engineering_method", "Quantum Algorithms",
     "applied_to", "Quantum computing innovation requires new algorithmic engineering exploiting superposition and entanglement.", 9),
    ("Technology Push", "engineering_method", "R&D Process",
     "applied_to", "Technology-push innovation is operationalised through R&D processes translating scientific discoveries into engineerable concepts.", 8),
    ("Demand Pull Innovation", "engineering_method", "User Research",
     "applied_to", "Demand-pull innovation relies on user research to surface latent needs that engineering teams translate into specifications.", 8),
    ("Biomimicry Innovation", "engineering_method", "Bioinspired Design",
     "theoretical_foundation", "Biomimicry innovation draws directly on bioinspired engineering: natural selection processes are translated into design heuristics.", 9),
    ("Circular Economy Innovation", "engineering_method", "Design for Disassembly",
     "applied_to", "Circular economy innovation requires engineering design for disassembly: products must be architected for component recovery and reuse.", 8),
    ("Cybersecurity Innovation", "engineering_method", "Security Engineering",
     "applied_to", "Cybersecurity innovation is operationalised through security-by-design engineering applied across the software development lifecycle.", 8),
    ("Neurotechnology Innovation", "engineering_method", "Human-Robot Interaction",
     "applied_to", "Neurotechnology innovation draws on human-robot interaction engineering for brain-computer interface design.", 7),
    ("AI Innovation", "engineering_method", "Explainable AI",
     "applied_to", "Responsible AI innovation requires explainable AI engineering to make model decisions transparent and auditable.", 9),
    ("Energy Innovation", "engineering_method", "Solar Energy",
     "applied_to", "Energy innovation includes solar photovoltaic engineering as a key implementation path for renewable transition.", 9),
    ("Data Innovation", "engineering_method", "Information Retrieval",
     "applied_to", "Data-driven innovation draws on information retrieval and recommendation system engineering to surface actionable insights.", 8),

    # ── innovation_theory ↔ humanities_concept ────────────────────────────
    ("Creative Destruction", "humanities_concept", "Dialectics",
     "philosophical_parallel", "Creative destruction enacts a dialectical movement: thesis (established order), antithesis (disruption), synthesis (new paradigm).", 8),
    ("Paradigm Shift", "humanities_concept", "Kuhnian Paradigm",
     "theoretical_foundation", "Dosi's technological paradigm directly borrows Kuhn's philosophy of science: normal vs. revolutionary technology follows the same logic.", 10),
    ("Technology and Society", "humanities_concept", "Social Construction of Technology",
     "theoretical_foundation", "SCOT provides the humanities-grounded counterpart to linear innovation models: technology is interpretively flexible.", 9),
    ("Tacit Knowledge", "humanities_concept", "Phenomenology",
     "philosophical_foundation", "Polanyi's tacit knowledge is grounded in Merleau-Ponty's phenomenology of skilled practice: knowing is embodied.", 9),
    ("Organisational Memory", "humanities_concept", "Memory Studies",
     "conceptual_parallel", "Organisational memory theory parallels memory studies: both examine how past experience is encoded, stored, retrieved, and forgotten.", 8),
    ("Innovation Narrative", "humanities_concept", "Narrative Theory",
     "applied_to", "Innovation strategy relies on narrative theory: compelling future stories create legitimacy and mobilise resources.", 8),
    ("Responsible Innovation", "humanities_concept", "Applied Ethics",
     "normative_foundation", "Responsible innovation is normatively grounded in applied ethics: bioethics, environmental ethics, and technology ethics.", 9),
    ("Intellectual Property", "humanities_concept", "Philosophy of Property",
     "philosophical_foundation", "IP regimes rest on philosophical theories: Lockean labour mixing, Hegelian personality theory, and utilitarian incentive arguments.", 9),
    ("Philosophy of Technology", "humanities_concept", "Critical Theory",
     "philosophical_foundation", "Critical theory interrogates how innovation under capitalism perpetuates instrumental rationality and commodity fetishism.", 8),
    ("Innovation History", "humanities_concept", "Historiography",
     "methodological_foundation", "History of technology employs historiographical methods—periodisation, source criticism, counterfactuals—to narrate technological change.", 9),
    ("Knowledge Commons", "humanities_concept", "Commons Theory",
     "theoretical_foundation", "Innovation commons theory draws on humanistic commons scholarship to govern shared knowledge pools without privatisation.", 9),
    ("Technological Imagination", "humanities_concept", "Social Imaginaries",
     "conceptual_parallel", "The sociology of expectations in innovation mirrors social imaginaries: shared visions of technological futures coordinate investment.", 9),
    ("Technology Ethics", "humanities_concept", "Virtue Ethics",
     "applied_to", "Responsible technology innovation draws on virtue ethics to define the character traits (prudence, justice, care) innovators ought to cultivate.", 8),
    ("Digital Innovation", "humanities_concept", "Philosophy of Information",
     "philosophical_foundation", "Digital innovation raises questions in philosophy of information: data ontology, informational privacy, and algorithmic ethics.", 8),
    ("Open Science", "humanities_concept", "Hermeneutics",
     "methodological_parallel", "Open science enacts hermeneutic principles: interpretive communities around shared datasets produce richer, self-correcting knowledge.", 7),
    ("Innovation and Culture", "humanities_concept", "Cultural Studies",
     "applied_to", "Cultural studies analyses how cultural values, aesthetics, and power relations shape what innovations are developed.", 8),
    ("Futures Studies Innovation", "humanities_concept", "Utopia",
     "conceptual_parallel", "Anticipatory innovation governance uses utopian and dystopian narratives to negotiate socially desirable technological futures.", 7),
    ("Convergence Technology", "humanities_concept", "Transhumanism",
     "philosophical_debate", "NBIC convergence innovations raise transhumanist questions about the boundaries of the human—enhancement challenges humanist ethics.", 7),
    ("Biomimicry", "humanities_concept", "Philosophy of Nature",
     "philosophical_foundation", "Biomimicry draws on philosophical traditions—from Aristotle's teleology to deep ecology—that attribute normative force to natural processes.", 7),
    ("Knowledge Management", "humanities_concept", "Hermeneutics",
     "methodological_foundation", "Knowledge management draws on hermeneutic methods: interpreting organisational texts to surface tacit assumptions.", 7),
    ("Grassroots Innovation", "humanities_concept", "Political Philosophy",
     "normative_foundation", "Grassroots innovation is normatively grounded in political philosophy of justice, participation, and collective self-determination.", 7),
    ("Social Innovation", "humanities_concept", "Political Philosophy",
     "normative_foundation", "Social innovation is normatively grounded in political philosophy of justice and the common good.", 7),
    ("Innovation Policy", "humanities_concept", "Political Economy",
     "applied_to", "Innovation policy is shaped by political economy structures, power relations, and distributional interests.", 8),
    ("Technology and Labor", "humanities_concept", "Labor History",
     "historical_connection", "Technology innovation history intersects with labour history: mechanisation, automation, and deskilling are perennial concerns.", 8),
    ("Sustainable Innovation", "humanities_concept", "Environmental Ethics",
     "normative_foundation", "Sustainable innovation is normatively grounded in environmental ethics: obligations to future generations and non-human nature.", 9),

    # ── innovation_theory ↔ natural_discovery ─────────────────────────────
    ("Technology Life Cycle", "natural_discovery", "Logistic Growth Model",
     "mathematical_analogy", "The technology S-curve is a logistic growth equation: adoption follows sigmoid dynamics analogous to population growth in resource-limited environments.", 9),
    ("Evolutionary Innovation", "natural_discovery", "Natural Selection",
     "theoretical_analogy", "Nelson & Winter's evolutionary theory directly borrows natural selection logic: routines vary, markets select, successful variants proliferate.", 10),
    ("Complex Adaptive Systems", "natural_discovery", "Complexity Theory",
     "theoretical_foundation", "Innovation ecosystems are complex adaptive systems: emergent order arises from local interactions among heterogeneous agents.", 9),
    ("Niche Innovation", "natural_discovery", "Ecological Niche Theory",
     "theoretical_analogy", "Strategic niche management directly borrows ecological niche theory: protected experimental spaces shelter emerging technologies.", 9),
    ("Innovation and Entropy", "natural_discovery", "Thermodynamics",
     "theoretical_analogy", "Information-theoretic measures of innovation diversity (variety, balance, disparity) borrow entropy concepts from thermodynamics.", 8),
    ("Network Innovation", "natural_discovery", "Network Science",
     "methodological_foundation", "Innovation network analysis draws on network science—scale-free topology, preferential attachment—to explain knowledge diffusion.", 9),
    ("Patent Citation Networks", "natural_discovery", "Citation Network Analysis",
     "methodological_foundation", "Patent citation analysis applies bibliometric methods from natural science to map technological relatedness and knowledge flow.", 9),
    ("Bibliometrics and Innovation", "natural_discovery", "Scientometrics",
     "methodological_foundation", "Innovation measurement via scientometrics uses citation analysis, h-index, and co-authorship networks from natural science methodology.", 9),
    ("Technological Convergence", "natural_discovery", "Convergent Evolution",
     "theoretical_analogy", "Technological convergence mirrors convergent evolution: independent technology lineages evolve similar solutions to shared functional constraints.", 7),
    ("Probabilistic Innovation", "natural_discovery", "Bayesian Inference",
     "methodological_foundation", "Technology forecasting uses Bayesian inference to update probability estimates of technical success as evidence accumulates.", 9),
    ("Swarm Intelligence", "natural_discovery", "Collective Behaviour",
     "theoretical_analogy", "Swarm intelligence models of collective innovation draw on studies of collective behaviour in social insects.", 8),
    ("Simulation-Based Innovation", "natural_discovery", "Agent-Based Modelling",
     "methodological_foundation", "Agent-based modelling from ecology enables simulation of innovation diffusion, market dynamics, and technology competition.", 9),
    ("Energy Innovation", "natural_discovery", "Thermodynamics",
     "applied_to", "Energy innovation is constrained by thermodynamic limits: Carnot efficiency and exergy analysis define the physical performance envelope.", 9),
    ("Materials Innovation", "natural_discovery", "Condensed Matter Physics",
     "applied_to", "Materials innovation (semiconductors, superconductors) is grounded in condensed matter physics discoveries.", 9),
    ("Biotechnology Innovation", "natural_discovery", "Molecular Biology",
     "applied_to", "Biotechnology innovation operationalises molecular biology: CRISPR, PCR, and recombinant DNA are science-to-technology translations.", 10),
    ("Quantum Technology Innovation", "natural_discovery", "Quantum Physics",
     "applied_to", "Quantum technology innovation derives entirely from quantum physics discoveries about superposition and entanglement.", 10),
    ("Climate Innovation", "natural_discovery", "Earth System Science",
     "applied_to", "Climate-mitigation innovation is guided by earth system science: carbon budgets and planetary boundaries define the solution space.", 9),
    ("Neurotechnology Innovation", "natural_discovery", "Neuroscience",
     "applied_to", "Neurotechnology innovation directly applies neuroscience discoveries about neural coding and plasticity.", 9),
    ("Pandemic Innovation", "natural_discovery", "Epidemiology",
     "applied_to", "Pandemic-response innovations (mRNA vaccines) are enabled by epidemiological models guiding resource allocation and trial design.", 9),
    ("Space Technology Innovation", "natural_discovery", "Astrophysics",
     "applied_to", "Space technology innovation is grounded in astrophysics: orbital mechanics and propulsion physics constrain design.", 9),
    ("Synthetic Biology Innovation", "natural_discovery", "Systems Biology",
     "applied_to", "Synthetic biology applies systems biology modelling to engineer novel biological systems with desired functional properties.", 9),
    ("AI and Cognitive Science", "natural_discovery", "Cognitive Science",
     "theoretical_foundation", "AI-driven innovation draws on cognitive science models of perception, learning, and reasoning—connectionism, Bayesian brain.", 8),
    ("Open Science and Replication", "natural_discovery", "Replication Crisis",
     "applied_to", "Open innovation policy learns from natural science's replication crisis: pre-registration and open data norms are adopted in applied research.", 8),
    ("Genetic Algorithm Optimisation", "natural_discovery", "Evolutionary Biology",
     "mathematical_analogy", "Genetic algorithms used in engineering innovation search are direct mathematical analogies of biological evolution.", 9),
    ("Self-Organisation", "natural_discovery", "Self-Organised Criticality",
     "theoretical_analogy", "Innovation clusters exhibit self-organised criticality: cascades of creative destruction follow power-law distributions.", 7),

    # ── innovation_theory ↔ arts_question ─────────────────────────────────
    ("Design Thinking", "arts_question", "Human-Centered Design",
     "theoretical_foundation", "Design thinking emerged from HCD practice in industrial design: IDEO's methodology translated studio critique into a business innovation process.", 10),
    ("Creative Economy", "arts_question", "Creative Industries",
     "theoretical_foundation", "Creative economy theory is grounded in arts practice: creative industries research analyses how cultural production generates economic value.", 9),
    ("Aesthetic Innovation", "arts_question", "Aesthetics",
     "conceptual_parallel", "Aesthetic innovation in product design draws on philosophical aesthetics: beauty, form, and sensory experience are competitive differentiators.", 8),
    ("Prototype Theory", "arts_question", "Speculative Design",
     "methodological_parallel", "Innovation prototyping and speculative design converge: both use tangible artefacts to make future possibilities concrete and contestable.", 8),
    ("Open Innovation", "arts_question", "Participatory Art",
     "conceptual_parallel", "Open innovation and participatory art share co-creation logic: external contributors add value beyond what the originating organisation can produce alone.", 7),
    ("User Experience Innovation", "arts_question", "Interactive Design",
     "applied_to", "UX innovation draws on interactive design principles—affordance, feedback, constraints—from arts and HCI to create intuitive interfaces.", 9),
    ("Gamification Innovation", "arts_question", "Game Studies",
     "applied_to", "Innovation through gamification applies game design principles (mechanics, dynamics, aesthetics) to non-game contexts to drive engagement.", 9),
    ("Music Technology Innovation", "arts_question", "Electronic Music",
     "applied_to", "Music technology innovation (synthesisers, DAWs, streaming) emerges from creative demands of electronic music composers.", 8),
    ("Architectural Innovation", "arts_question", "Architecture",
     "applied_to", "Architectural innovation generates building typologies and structural systems reshaping the built environment.", 8),
    ("Film and Media Innovation", "arts_question", "Film Theory",
     "applied_to", "Media innovation (streaming, VR cinema) is theorised through film theory frameworks adapted to emerging screen technologies.", 7),
    ("Social Innovation and Arts", "arts_question", "Community Arts",
     "applied_to", "Social innovation draws on community arts practice: participatory arts develop collective creativity and civic problem-solving.", 8),
    ("Future Foresight", "arts_question", "Speculative Design",
     "methodological_parallel", "Innovation foresight and speculative design share anticipatory logic: artefacts from imagined futures probe assumptions.", 9),
    ("Data Innovation", "arts_question", "Data Visualisation",
     "applied_to", "Data-driven innovation is communicated through data visualisation applying information design principles from the arts.", 8),
    ("Wearable Technology Innovation", "arts_question", "Fashion Design",
     "applied_to", "Wearable technology innovation sits at the intersection of electronics engineering and fashion design.", 8),
    ("Creative AI", "arts_question", "AI Art",
     "applied_to", "Creative AI innovation is driven by artistic experimentation: AI art practitioners push generative model capabilities in ways that feed back into research.", 9),
    ("Service Design Innovation", "arts_question", "Service Design",
     "theoretical_foundation", "Service design, originating in design schools, provides the toolkit for service innovation: journey mapping and touchpoint co-design.", 9),
    ("Brand Innovation", "arts_question", "Visual Identity",
     "applied_to", "Brand innovation is executed through visual identity design: logo, colour system, and typographic choices create distinctive positioning.", 8),
    ("Augmented Reality Innovation", "arts_question", "Mixed Reality Art",
     "applied_to", "AR innovation is co-developed by artists and technologists: mixed-reality art installations prototype experiential modalities later deployed commercially.", 8),
    ("Sound Innovation", "arts_question", "Sound Art",
     "applied_to", "Sound innovation in product design draws on sound art practices treating sonic environment as a designed experiential medium.", 7),
    ("Sustainable Design Innovation", "arts_question", "Sustainable Design",
     "applied_to", "Sustainable innovation draws on sustainable design from arts schools: material reduction, repairability, and aesthetic durability.", 9),
    ("Narrative Innovation", "arts_question", "Narrative Theory",
     "applied_to", "Narrative theory from literary arts is applied in innovation management to craft product stories and organisational change narratives.", 8),
    ("Visual Innovation", "arts_question", "Visual Art",
     "applied_to", "Visual innovation in product and UI design draws on fine art traditions—colour theory, composition, semiotics.", 8),
    ("Typography and Communication Innovation", "arts_question", "Typography",
     "applied_to", "Innovation in digital communication relies on typographic principles from graphic arts for legibility and brand coherence.", 7),
    ("Interaction Innovation", "arts_question", "Body and Performance Art",
     "conceptual_parallel", "Interaction design innovation and performance art both study embodied human action: gesture and movement as communicative modalities.", 7),
    ("Biomimicry Design", "arts_question", "Biomorphic Art",
     "conceptual_parallel", "Biomimicry innovation and biomorphic art both translate natural forms into human-made structures.", 7),
]


# ─────────────────────────────────────────────────────────────────────────────
# Subfield-to-subfield affinity rules for bulk programmatic relations
# (inno_subfield_kw, target_table, target_subfield_kw,
#  relation_type, strength, desc)
# ─────────────────────────────────────────────────────────────────────────────
SUBFIELD_AFFINITIES = [
    # innovation → social_theory
    ("neo_schumpeterian", "social_theory", "制度論", "theoretical_foundation", 8,
     "Neo-Schumpeterian economics and institutionalist theory jointly explain how institutions shape innovation trajectories."),
    ("neo_schumpeterian", "social_theory", "経路依存", "theoretical_foundation", 9,
     "Path dependence in neo-Schumpeterian economics mirrors historical institutionalist analysis of lock-in."),
    ("neo_schumpeterian", "social_theory", "経済学", "theoretical_foundation", 8,
     "Neo-Schumpeterian innovation economics is grounded in evolutionary economic theory."),
    ("innovation_systems", "social_theory", "社会的ネットワーク", "methodological_foundation", 7,
     "Innovation systems research uses SNA to map actor relations and knowledge flows."),
    ("innovation_systems", "social_theory", "制度論", "theoretical_foundation", 8,
     "National Innovation Systems depend on institutional frameworks for knowledge governance."),
    ("knowledge_learning", "social_theory", "社会的ネットワーク", "conceptual_parallel", 7,
     "Knowledge networks in innovation parallel social network structures of information diffusion."),
    ("open_innovation", "social_theory", "取引費用", "theoretical_foundation", 8,
     "Open innovation reduces transaction costs for knowledge exchange across firm boundaries."),
    ("platform_digital", "social_theory", "取引費用", "theoretical_foundation", 8,
     "Digital platform innovation is governed by transaction cost logic and multi-sided market theory."),
    ("platform_digital", "social_theory", "ゲーム理論", "applied_to", 7,
     "Platform competition is modelled as game theory with network externalities."),
    ("entrepreneurship", "social_theory", "制度論", "applied_to", 8,
     "Institutional entrepreneurship bridges Schumpeterian and sociological theories of change."),
    ("sustainability_transitions", "social_theory", "社会運動", "theoretical_parallel", 7,
     "Sustainability transitions share dynamics with social movements: niche actors challenge regime incumbents."),
    ("sustainability_transitions", "social_theory", "制度論", "theoretical_foundation", 8,
     "Sustainability transitions require institutional change: new regulatory and normative frameworks."),
    ("measurement_policy", "social_theory", "政策", "applied_to", 7,
     "Innovation policy design draws on social science theories of governance and collective action."),
    ("diffusion_adoption", "social_theory", "社会的影響", "theoretical_foundation", 8,
     "Innovation diffusion theory is grounded in social influence and conformity mechanisms."),
    ("open_innovation_ecosystems", "social_theory", "社会関係資本", "conceptual_parallel", 7,
     "Open innovation ecosystems depend on social capital to coordinate voluntary knowledge exchange."),
    ("sectoral_innovation", "social_theory", "産業・組織", "conceptual_parallel", 7,
     "Sectoral innovation patterns parallel organisational sociology's analysis of industry field structures."),
    ("institutional_economics", "social_theory", "制度論", "theoretical_foundation", 9,
     "Institutional economics and new institutionalism share the core proposition that institutions shape economic behaviour."),
    ("entrepreneurship_venture", "social_theory", "社会移動", "theoretical_parallel", 7,
     "Entrepreneurship as social mobility mechanism mirrors sociological analysis of upward status transitions."),

    # innovation → engineering_method
    ("process_management", "engineering_method", "アジャイル", "methodological_parallel", 8,
     "Innovation process management and agile engineering share iterative, feedback-driven logic."),
    ("platform_digital", "engineering_method", "クラウド", "applied_to", 8,
     "Digital platform innovation is implemented through cloud engineering infrastructure."),
    ("platform_digital", "engineering_method", "深層学習", "applied_to", 8,
     "AI-driven digital innovation is operationalised through deep learning engineering methods."),
    ("technology_paradigms", "engineering_method", "設計", "conceptual_parallel", 7,
     "Technology paradigms co-evolve with dominant engineering design architectures."),
    ("disruptive_innovation", "engineering_method", "アーキテクチャ", "theoretical_foundation", 8,
     "Disruptive innovation analysis requires understanding architectural dependencies in technology systems."),
    ("sustainability_transitions", "engineering_method", "太陽光", "applied_to", 9,
     "Sustainability transitions are implemented through renewable energy engineering innovations."),
    ("sustainability_transitions", "engineering_method", "水素", "applied_to", 8,
     "Hydrogen energy systems are a key engineering innovation in sustainability transitions."),
    ("open_innovation_ecosystems", "engineering_method", "API", "applied_to", 8,
     "Open innovation ecosystems are technically implemented through open API architectures."),
    ("knowledge_learning", "engineering_method", "機械学習", "applied_to", 8,
     "Machine learning methods operationalise knowledge extraction in innovation analytics."),
    ("measurement_policy", "engineering_method", "データ", "applied_to", 7,
     "Innovation measurement and policy rely on data engineering methods for large-scale indicator tracking."),
    ("diffusion_adoption", "engineering_method", "ユーザビリティ", "applied_to", 7,
     "Innovation adoption is facilitated by usability engineering that removes friction barriers."),
    ("entrepreneurship_venture", "engineering_method", "DevOps", "applied_to", 7,
     "Venture-backed startups leverage DevOps engineering to accelerate product iteration cycles."),
    ("open_innovation", "engineering_method", "バージョン管理", "applied_to", 8,
     "Open source innovation depends on version control engineering for distributed collaboration."),
    ("sectoral_innovation", "engineering_method", "CRISPR", "applied_to", 9,
     "Biotechnology sector innovation is operationalised through CRISPR and genome editing engineering."),
    ("sustainability_transitions_social", "engineering_method", "ライフサイクル", "applied_to", 8,
     "Sociotechnical sustainability transitions require LCA engineering to verify environmental claims."),

    # innovation → humanities_concept
    ("neo_schumpeterian", "humanities_concept", "political_economy", "theoretical_foundation", 8,
     "Neo-Schumpeterian economics intersects with political economy in explaining capitalist dynamics."),
    ("neo_schumpeterian", "humanities_concept", "STS", "theoretical_parallel", 8,
     "Neo-Schumpeterian innovation history connects with STS accounts of technology-society co-evolution."),
    ("technology_paradigms", "humanities_concept", "科学哲学", "philosophical_foundation", 9,
     "Technological paradigm theory is grounded in philosophy of science epistemology."),
    ("innovation_systems", "humanities_concept", "political_economy", "applied_to", 7,
     "National innovation systems are shaped by political economy structures and power relations."),
    ("sustainability_transitions", "humanities_concept", "環境人類学", "applied_to", 8,
     "Sustainability transitions engage environmental anthropology and political ecology perspectives."),
    ("knowledge_learning", "humanities_concept", "認知人類学", "theoretical_foundation", 7,
     "Knowledge and learning in innovation draw on cognitive anthropology's accounts of distributed cognition."),
    ("entrepreneurship", "humanities_concept", "経済人類学", "theoretical_foundation", 7,
     "Entrepreneurship theory connects to economic anthropology's analysis of exchange and value creation."),
    ("sustainability_transitions_social", "humanities_concept", "倫理学", "normative_foundation", 8,
     "Sociotechnical sustainability transitions are normatively grounded in environmental and intergenerational ethics."),
    ("diffusion_adoption", "humanities_concept", "文化人類学", "theoretical_foundation", 7,
     "Innovation diffusion across cultures draws on cultural anthropology's analysis of meaning-making and adoption."),
    ("measurement_policy_governance", "humanities_concept", "政治哲学", "normative_foundation", 7,
     "Innovation governance draws on political philosophy for legitimacy, accountability, and justice principles."),
    ("institutional_economics_voc", "humanities_concept", "social_theory", "theoretical_foundation", 7,
     "Varieties of capitalism institutionalism connects to social theory of embedded economic action."),
    ("open_innovation", "humanities_concept", "デジタル人類学", "applied_to", 7,
     "Open innovation in digital spaces is studied through digital anthropology's ethnographic methods."),

    # innovation → natural_discovery
    ("neo_schumpeterian", "natural_discovery", "進化生物学", "theoretical_analogy", 9,
     "Nelson & Winter's evolutionary economics directly analogises biological evolutionary theory."),
    ("complex_adaptive", "natural_discovery", "ネットワーク科学", "methodological_foundation", 9,
     "Innovation network analysis draws on network science methods from physics and biology."),
    ("technology_paradigms", "natural_discovery", "カオス", "theoretical_analogy", 7,
     "Technological transitions exhibit punctuated equilibrium dynamics analogous to chaos theory."),
    ("sustainability_transitions", "natural_discovery", "気候変動", "applied_to", 9,
     "Climate change mitigation drives sustainability transitions through carbon constraint innovation."),
    ("sustainability_transitions", "natural_discovery", "生態系", "applied_to", 8,
     "Ecological resilience concepts from ecology inform sociotechnical transition theory."),
    ("knowledge_learning", "natural_discovery", "ベイズ", "methodological_foundation", 8,
     "Bayesian learning models are applied in innovation forecasting and R&D decision-making."),
    ("measurement_policy", "natural_discovery", "統計", "methodological_foundation", 8,
     "Innovation measurement draws on statistical methods from natural science for valid indicators."),
    ("platform_digital", "natural_discovery", "量子情報", "applied_to", 8,
     "Quantum computing platforms represent the frontier of digital innovation grounded in quantum physics."),
    ("innovation_systems", "natural_discovery", "ネットワーク科学", "methodological_foundation", 8,
     "Innovation system mapping uses network science metrics (centrality, clustering) to evaluate system structure."),
    ("sectoral_innovation", "natural_discovery", "タンパク質構造", "applied_to", 8,
     "Pharmaceutical sector innovation is driven by protein structure prediction discoveries."),
    ("sectoral_innovation", "natural_discovery", "CRISPR", "applied_to", 9,
     "Life science sector innovation is fundamentally enabled by CRISPR genome editing technologies."),
    ("sustainability_transitions_social", "natural_discovery", "保全生態学", "applied_to", 7,
     "Biodiversity-related social innovation is grounded in conservation ecology science."),
    ("disruptive_innovation_dynamics", "natural_discovery", "相転移", "theoretical_analogy", 7,
     "Disruptive innovation dynamics exhibit phase transition analogues: systems rapidly shift to new equilibria."),

    # innovation → arts_question
    ("design_thinking", "arts_question", "人間中心", "theoretical_foundation", 10,
     "Design thinking is the meta-framework within which human-centered design arts practices are applied."),
    ("platform_digital", "arts_question", "AIアート", "applied_to", 8,
     "Digital platform innovation enables AI art creation and distribution at scale."),
    ("creative_economy", "arts_question", "音楽産業", "theoretical_foundation", 8,
     "Creative economy theory analyses how music industry platform innovation restructures cultural value chains."),
    ("sustainability", "arts_question", "サステナブルデザイン", "applied_to", 9,
     "Sustainable innovation mandates sustainable design principles in product and service creation."),
    ("user_experience", "arts_question", "サービスデザイン", "applied_to", 9,
     "UX innovation and service design share methods for co-creating meaningful human experiences."),
    ("open_innovation", "arts_question", "コデザイン", "conceptual_parallel", 8,
     "Open innovation and co-design converge: both invite external stakeholders into the creative process."),
    ("social_innovation", "arts_question", "ソーシャリー", "applied_to", 8,
     "Social innovation connects with socially engaged art: both use participatory creative methods for social change."),
    ("diffusion_adoption", "arts_question", "ゲームスタディ", "applied_to", 7,
     "Innovation adoption in gaming platforms is studied through game studies frameworks."),
    ("digital_innovation", "arts_question", "データ美学", "applied_to", 7,
     "Digital innovation in data presentation draws on data aesthetics and information design principles."),
    ("entrepreneurship_venture", "arts_question", "スペクタクル", "conceptual_parallel", 6,
     "Startup culture shares spectacle theory characteristics: performance of disruption as brand identity."),
    ("sectoral_innovation", "arts_question", "映像", "applied_to", 7,
     "Media sector innovation drives new forms of visual storytelling and interactive narrative."),
    ("open_innovation_ecosystems", "arts_question", "パフォーマンス", "conceptual_parallel", 6,
     "Open innovation ecosystems share performative qualities: actors enact roles in a co-created innovation drama."),
    ("measurement_policy_governance", "arts_question", "情報デザイン", "applied_to", 7,
     "Innovation policy communication relies on information design to make complex metrics accessible."),
]


def load_table(conn, table):
    cur = conn.cursor()
    cols = [row[1] for row in cur.execute(f"PRAGMA table_info({table})").fetchall()]
    fields = ["id"]
    for col in ["name_en", "keywords_en", "subfield"]:
        if col in cols:
            fields.append(col)
    rows = cur.execute(f"SELECT {', '.join(fields)} FROM {table}").fetchall()
    return [dict(zip(fields, r)) for r in rows]


def find_id(rows, fragment):
    """Find best matching row by name_en substring."""
    frag_lower = fragment.lower()
    for r in rows:
        if r.get("name_en") and frag_lower in r["name_en"].lower():
            return r["id"]
    return None


def already_exists_set(existing_set, sid, tid):
    return (sid, tid) in existing_set


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")

    print("Loading tables...")
    inno_rows = load_table(conn, "innovation_theory")
    print(f"  innovation_theory: {len(inno_rows)} rows")

    tables = ["social_theory", "engineering_method", "humanities_concept",
              "natural_discovery", "arts_question"]
    table_data = {}
    for tbl in tables:
        rows = load_table(conn, tbl)
        table_data[tbl] = rows
        print(f"  {tbl}: {len(rows)} rows")

    # Load existing pairs into a set for fast dedup
    cur = conn.cursor()
    existing = cur.execute(
        "SELECT source_id, target_id FROM cross_domain_relations "
        "WHERE source_domain='innovation_theory'"
    ).fetchall()
    existing_set = set((r[0], r[1]) for r in existing)
    print(f"\nExisting innovation_theory relations: {len(existing_set)}")

    to_insert = []
    seen = set(existing_set)

    def add(sid, ttable, tid, rtype, desc, strength):
        key = (sid, tid)
        if key in seen:
            return
        seen.add(key)
        to_insert.append((
            make_id(), "innovation_theory", sid, ttable, tid,
            rtype, desc[:400], strength, now_str()
        ))

    # ── 1. Curated relations ──────────────────────────────────────────────
    print("\nBuilding curated relations...")
    curated_count = 0
    for (ifrag, ttable, tfrag, rtype, desc, strength) in CURATED:
        iid = find_id(inno_rows, ifrag)
        tid = find_id(table_data[ttable], tfrag)
        if iid and tid:
            add(iid, ttable, tid, rtype, desc, strength)
            curated_count += 1
        else:
            pass  # silently skip unmatched
    print(f"  Curated matched: {curated_count}")

    # ── 2. Subfield-affinity bulk relations ───────────────────────────────
    print("Building subfield-affinity relations...")
    aff_count = 0
    for (isf, ttable, tsf, rtype, strength, desc) in SUBFIELD_AFFINITIES:
        isf_l = isf.lower()
        tsf_l = tsf.lower()
        # matching inno rows
        m_inno = [r for r in inno_rows
                  if isf_l in (r.get("subfield") or "").lower()
                  or isf_l in (r.get("name_en") or "").lower()][:15]
        # matching target rows
        m_tgt = [r for r in table_data[ttable]
                 if tsf_l in (r.get("subfield") or "").lower()
                 or tsf_l in (r.get("name_en") or "").lower()
                 or tsf_l in (r.get("keywords_en") or "").lower()][:10]
        for ir in m_inno:
            for tr in m_tgt:
                full_desc = f"{desc} (cf. {tr.get('name_en', tr['id'])})"
                add(ir["id"], ttable, tr["id"], rtype, full_desc, strength)
                aff_count += 1
    print(f"  Subfield-affinity pairs generated: {aff_count}")

    # ── 3. Cross-keyword matching (capped for performance) ────────────────
    print("Building keyword-match relations (capped)...")

    KEYWORD_PAIRS = [
        # (inno_kw_list, target_table, target_kw_list, rel_type, strength, desc_prefix, max_pairs)
        (["organizational learning", "knowledge creation", "knowledge management"],
         "social_theory", ["knowledge", "learning", "organization"],
         "theoretical_foundation", 7, "Organizational knowledge concepts in innovation connect to", 30),
        (["network", "ecosystem", "alliance", "collaboration"],
         "social_theory", ["network", "social capital", "tie"],
         "conceptual_parallel", 7, "Network-based innovation theory connects to social network perspectives in", 30),
        (["sustainability", "transition", "green", "circular"],
         "social_theory", ["ecology", "environment", "climate"],
         "applied_to", 7, "Sustainability transitions draw on socio-ecological frameworks in", 25),
        (["digital", "platform", "software", "data"],
         "engineering_method", ["software", "cloud", "data", "system"],
         "applied_to", 7, "Digital innovation is implemented through engineering methods in", 40),
        (["process", "stage", "agile", "lean"],
         "engineering_method", ["process", "agile", "pipeline", "lifecycle"],
         "methodological_parallel", 7, "Innovation process management aligns with engineering frameworks in", 25),
        (["responsible", "ethics", "inclusive", "social value"],
         "humanities_concept", ["ethics", "moral", "justice"],
         "normative_foundation", 7, "Responsible innovation draws normative guidance from humanistic frameworks in", 30),
        (["philosophy", "epistemol", "paradigm", "theory"],
         "humanities_concept", ["philosophy", "epistemol", "theory", "paradigm"],
         "philosophical_foundation", 7, "Innovation theory epistemology connects to philosophical traditions in", 25),
        (["evolution", "adaptive", "selection", "variation", "fitness"],
         "natural_discovery", ["evolution", "selection", "adaptation", "fitness"],
         "theoretical_analogy", 8, "Evolutionary innovation theory draws direct analogies from biological concepts in", 35),
        (["complex", "system", "emergence", "network", "nonlinear"],
         "natural_discovery", ["complexity", "emergence", "system", "network"],
         "theoretical_analogy", 7, "Innovation systems as complex adaptive systems draw on natural science in", 30),
        (["design", "creative", "aesthetic", "user experience"],
         "arts_question", ["design", "creative", "aesthetic", "user"],
         "applied_to", 7, "Creative and design innovation connects to arts practices in", 35),
        (["technology", "digital", "media", "platform"],
         "arts_question", ["digital", "media", "technology", "AI"],
         "applied_to", 7, "Digital technology innovation intersects with digital arts practices in", 30),
    ]

    kw_count = 0
    for (ikws, ttable, tkws, rtype, strength, prefix, max_p) in KEYWORD_PAIRS:
        m_inno = []
        for r in inno_rows:
            txt = ((r.get("name_en") or "") + " " + (r.get("keywords_en") or "")).lower()
            if any(kw.lower() in txt for kw in ikws):
                m_inno.append(r)

        m_tgt = []
        for r in table_data[ttable]:
            txt = ((r.get("name_en") or "") + " " + (r.get("keywords_en") or "") + " " + (r.get("subfield") or "")).lower()
            if any(kw.lower() in txt for kw in tkws):
                m_tgt.append(r)

        count = 0
        for ir in m_inno:
            for tr in m_tgt:
                if count >= max_p:
                    break
                desc = f"{prefix} {tr.get('name_en', tr['id'])}."
                add(ir["id"], ttable, tr["id"], rtype, desc, strength)
                count += 1
                kw_count += 1
            if count >= max_p:
                break

    print(f"  Keyword-match pairs generated: {kw_count}")

    # ── Batch insert ──────────────────────────────────────────────────────
    print(f"\nInserting {len(to_insert)} new relations...")
    conn.executemany("""
        INSERT OR IGNORE INTO cross_domain_relations
        (id, source_domain, source_id, target_domain, target_id,
         relation_type, relation_description, strength, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, to_insert)
    conn.commit()

    # ── Summary ───────────────────────────────────────────────────────────
    total = conn.execute(
        "SELECT COUNT(*) FROM cross_domain_relations WHERE source_domain='innovation_theory'"
    ).fetchone()[0]
    print(f"\nTotal innovation_theory relations: {total}")

    print("\nBreakdown by target table:")
    rows = conn.execute("""
        SELECT target_domain, COUNT(*) as cnt
        FROM cross_domain_relations
        WHERE source_domain='innovation_theory'
        GROUP BY target_domain
        ORDER BY cnt DESC
    """).fetchall()
    for r in rows:
        print(f"  innovation_theory → {r[0]}: {r[1]}")

    print("\nAll cross_domain_relations breakdown:")
    rows = conn.execute("""
        SELECT source_domain, target_domain, COUNT(*) as cnt
        FROM cross_domain_relations
        GROUP BY source_domain, target_domain
        ORDER BY source_domain, target_domain
    """).fetchall()
    for r in rows:
        print(f"  {r[0]} → {r[1]}: {r[2]}")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
