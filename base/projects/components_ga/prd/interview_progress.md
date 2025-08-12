# Dagster Components GA PRD - Interview Progress

**Date**: 2025-08-09  
**Status**: In Progress - Section 2 Complete, Section 3 Pending  
**Next Session**: Continue with Section 3 - Milestones

## Interview Sections Completed

### ✅ Section 1: Context (COMPLETED)

**Marketing Statement Direction**:

- Target: "Medium-code practitioners" (domain experts who use real programming languages but don't want to become platform experts)
- AI-native data platform positioning
- "Low-Code Convenience with High-Code Power"

**Key Context Answers**:

- **AI Integration**: Structured data/metadata for model building, less context required than competitors, schema-rich constrained codegen
- **Democratization**: Analytics engineers, data scientists using domain tools like dbt
- **Collaboration**: API/tooling ecosystem between platform teams and users, shared infrastructure
- **Competitive Pressure**: Airflow 3 + Prefect have asset-oriented features, need differentiation
- **Timeline**: Oct 15, 2025 target, RC banner adoption disincentive, internal milestone needs
- **Market Window**: Long-term epochal AI shift just starting
- **Stack Coverage**: Airflow has broader integration surface currently

### ✅ Section 2: Usage Scenarios (COMPLETED)

**Scenario 1: Foundation Model Training Company (e.g., Poolside-type)**

- **Users**: Data platform engineers (extremely talented) serving researchers/data scientists
- **Problem**: Researchers work in notebooks, don't want to learn Dagster
- **Solution**: Platform engineers write custom Components, researchers scaffold instances via YAML
- **Value**: Cross-cutting policy enforcement, metadata standards, observability integration, controlled compute configuration

**Scenario 2: Analytics Engineer Onboarding dbt**

- **User**: Analytics engineer with dbt/SQL expertise, not Dagster expert
- **Problem**: Need to onboard dbt project onto Dagster platform for universal lineage/tooling
- **Current Pain**: 50 lines of Python with strange abstractions + Python env setup
- **Components Solution**: Few lines of YAML configuration
- **Example YAML**:
  ```yaml
  type: dagster_dbt.DbtProjectComponent
  attributes:
    project: "{{ project_root }}/transform/jdbt"
    translation:
      key: "target/main/{{ node.name }}"
  ```

**Scenario 3: Platform Team Enabling Domain Teams**

- **Distribution Model**: Platform team authors Components in packages
- **Discovery**: `dg` tools for introspection, integrated documentation in web app
- **Custom Components Examples**:
  - dbt: Enforce metadata rules (every model has owner)
  - Notebooks: Observability integration, custom context, compute whitelisting, authentication

### 🔄 Section 3: Milestones (PENDING)

**Next Questions**:

- Current development status on GA blockers
- Which pillars/components already in progress vs. need to start
- Prioritization of three main pillars

## Key References Captured

- GA Strategy Final Plan
- GA Success Criteria Research
- Roadshow presentation messaging
- Blog post messaging
- Medium-code concept context

## Outstanding Items

- Advanced enterprise use case definition (TODO)
- Section 3 Milestones interview
- Final PRD document creation
