# Section 2: Usage Scenarios - Detailed Workflows

## Scenario 1: Foundation Model Training Company (Poolside-type)

### User Profile

- **Primary Users**: Data platform engineers (extremely talented engineers)
- **Stakeholders**: Researchers and data scientists
- **Technical Context**: Some formally trained engineers, all use Spark, also dbt users
- **Current Challenge**: Researchers work in notebooks, don't want to learn Dagster

### Problem Statement

Researchers are productive in notebook environments but need to move to production systems without becoming Dagster experts. Platform team needs to provide controlled, policy-compliant infrastructure.

### Components Workflow

1. **Platform Engineer Role**: Writes custom Components with embedded best practices
2. **Researcher Role**: Scaffolds instances of Components, configures via YAML
3. **Division of Responsibilities**: "As simple as possible but no simpler" - platform engineers control complexity exposure

### Value Delivered

- **Cross-cutting Policy**: Systemic enforcement via Custom Components
- **Metadata Standards**: Automatic compliance with organizational standards
- **Observability Integration**: Easy-to-use configuration for monitoring tools
- **Compute Configuration**: Easy ways to configure compute in controlled ways
- **Controlled Flexibility**: Researchers get power without complexity

### Workflow Pattern

```
Platform Engineer → Writes Custom Component (Python)
Researcher → Scaffolds Instance (dg scaffold)
Researcher → Configures YAML (simple parameters)
System → Enforces policies automatically
```

## Scenario 2: Analytics Engineer Onboarding dbt Project

### User Profile

- **Role**: Analytics Engineer
- **Skills**: dbt and SQL expertise, NOT Dagster expert
- **Goal**: Onboard dbt project onto Dagster platform

### Problem Statement

Need to integrate existing dbt project into broader Dagster platform for:

- Universal lineage visibility
- Operational tooling integration
- Analytics platform benefits
- Team collaboration

### Current Pain Points (Without Components)

- **Code Complexity**: ~50 lines of Python code required
- **Strange Abstractions**: Complex Dagster concepts to learn
- **Environment Setup**: Python environment configuration burden
- **Expertise Gap**: Need to become Dagster expert for simple integration

### Components Solution

**Simplicity**: Few lines of YAML configuration
**No Python Setup**: Minimal environment requirements

### Example YAML Configuration

```yaml
type: dagster_dbt.DbtProjectComponent

attributes:
  project: "{{ project_root }}/transform/jdbt"
  translation:
    key: "target/main/{{ node.name }}"
```

### Integration Requirements

- **Upstream Dependencies**: Configure connections to upstream data assets (may require naming convention alignment or lightweight config)
- **Downstream Integration**: Downstream stakeholders configure their assets to depend on dbt project assets
- **Lineage**: Automatic integration into platform lineage graph

### Value Delivered

- **Massive Simplification**: 50 lines of complex Python → few lines of YAML
- **No Python Environment**: Eliminates setup complexity
- **Automatic Integration**: Immediate platform benefits
- **Preserved Expertise**: Analytics engineer stays in domain comfort zone

## Scenario 3: Platform Team Enabling Domain Teams

### Organizational Structure

- **Platform Team**: Authors and maintains Components
- **Domain Teams**: Researchers, analytics engineers, data scientists
- **Distribution Model**: Package-based distribution with discovery tooling

### Platform Team Workflow

1. **Component Development**: Create reusable Components addressing common patterns
2. **Package Distribution**: Author Components in installable packages
3. **Documentation**: Integrated documentation in web application
4. **Discoverability**: Enable discovery through `dg` tooling introspection

### Custom Component Examples

#### For dbt Projects

- **Metadata Enforcement**: Every model must have an owner
- **Standards Compliance**: Automatic application of naming conventions
- **Quality Gates**: Built-in testing and validation requirements

#### For Notebook Workflows

- **Observability Integration**: Automatic connection to monitoring tools
- **Custom Context**: Pass along context that target runtime expects
- **Compute Whitelisting**: Controlled list of available compute configurations (memory, CPU, etc.)
- **Authentication**: Proper resource authentication in target runtime
- **Policy Enforcement**: Security and compliance requirements

### Discovery and Usage Pattern

```
Platform Team → Authors Component Package
Domain User → Lists available: `dg list components`
Domain User → Reviews documentation in web app
Domain User → Scaffolds instance: `dg scaffold defs`
Domain User → Configures YAML with approved parameters
System → Enforces platform policies automatically
```

### Value Delivered

- **Standardization**: Consistent patterns across organization
- **Governance**: Automatic policy enforcement
- **Productivity**: Domain users focus on business logic, not infrastructure
- **Control**: Platform team maintains oversight without bottlenecks
- **Scaling**: Reusable patterns reduce duplicate effort

## Cross-Scenario Patterns

### Common Workflow Elements

1. **Separation of Concerns**: Platform engineers handle complexity, domain users handle configuration
2. **YAML Interface**: Consistent, simple configuration layer
3. **Built-in Governance**: Automatic policy enforcement
4. **Progressive Disclosure**: Complexity hidden until needed
5. **Discovery Tooling**: Easy to find and understand available Components

### GA Readiness Indicators

- **Workflow Completeness**: All three scenarios work end-to-end
- **Documentation Quality**: Clear guidance for each persona
- **Tooling Maturity**: `dg` commands support full workflows
- **Integration Depth**: Seamless platform integration (lineage, observability, etc.)

## Outstanding Questions

- **Advanced Enterprise Use Case**: Need to define most sophisticated scenario demonstrating full Components power
- **Edge Cases**: Scenarios where Components might NOT be appropriate
- **Migration Workflows**: Existing system to Components transition patterns
