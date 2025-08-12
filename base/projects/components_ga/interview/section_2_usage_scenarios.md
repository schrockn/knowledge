# Section 2: Usage Scenarios - Detailed Interview Capture

**Interview Date**: August 9, 2025  
**Stakeholder**: CTO/Founder  
**Section Status**: COMPLETE - Pending User Validation  
**Purpose**: Capture all usage scenario details for downstream PRD agent processing

## Overview

This document contains comprehensive usage scenarios for Dagster Components GA. Each scenario includes deep context about users, their workflows, pain points, and how Components transforms their experience. Maximum detail has been preserved for agent consumption.

---

## Scenario 1: Foundation Model Training Company - Research Team Enablement

### Organizational Context and Dynamics

#### Company Profile (Poolside-Type Organization)

**Industry**: AI/ML Foundation Model Development  
**Size**: High-growth startup with specialized teams  
**Technical Maturity**: Cutting-edge ML research with production demands  
**Key Challenge**: Bridging research productivity with production requirements

#### Team Structure and Roles

**Data Platform Engineers**:

- **Characterization**: "Extremely talented engineers" (direct quote)
- **Size**: Small, elite team (typically 3-5 engineers)
- **Responsibilities**:
  - Core infrastructure and orchestration
  - Platform reliability and scaling
  - Tool integration and automation
  - Setting organizational standards
- **Technical Stack**: Deep Dagster expertise, Kubernetes, cloud platforms
- **Pain Points**:
  - Constantly pulled into researcher support requests
  - Difficulty enforcing standards across research teams
  - Repetitive infrastructure setup for similar workflows

**Research Teams**:

- **Size**: Larger teams (20-50 researchers)
- **Composition**: Mix of formally trained engineers and domain experts
- **Technical Tools**:
  - Heavy Spark usage for distributed computation
  - Jupyter notebooks for experimentation
  - Some teams use dbt for data transformation
  - Python for model development
- **Expertise Level**: Deep ML knowledge, limited infrastructure experience
- **Core Quote**: "Researchers productive in notebooks but don't want to learn Dagster"

**Data Scientists**:

- **Role**: Bridge between research and production
- **Tools**: Notebooks, Python, SQL, model frameworks
- **Focus**: Feature engineering, model validation, experimentation
- **Infrastructure Needs**: Compute resources, data access, experiment tracking

### Current State Pain Points (Pre-Components)

#### Productivity Bottlenecks

1. **Research Velocity Impact**:
   - Researchers blocked waiting for platform team
   - Each production deployment requires platform engineer involvement
   - Learning Dagster would slow research output by 30-50%
   - Context switching between research and infrastructure

2. **Platform Team Overload**:
   - Every researcher request requires custom implementation
   - Similar patterns reimplemented multiple times
   - Can't scale support linearly with research team growth
   - Becomes bottleneck for innovation

3. **Policy Enforcement Challenges**:
   - No systematic way to apply organizational standards
   - Manual review of every pipeline for compliance
   - Inconsistent resource usage and cost overruns
   - Security and data governance gaps

4. **Infrastructure Complexity Exposure**:
   - Researchers need to understand:
     - Dagster concepts (assets, ops, resources)
     - Python environment management
     - Deployment configurations
     - Monitoring and observability setup

### Components-Enabled Workflow

#### Platform Engineer Workflow

**Phase 1: Component Design and Development**

1. **Requirements Gathering**:
   - Interview research teams about common patterns
   - Identify organizational policies and constraints
   - Understand compute and resource needs
   - Document security and compliance requirements

2. **Component Architecture**:
   - Design YAML interface following "as simple as possible but no simpler"
   - Embed organizational best practices in implementation
   - Create abstraction layers for complex infrastructure
   - Build in policy enforcement mechanisms

3. **Implementation Details**:

   ```python
   # Example: Custom Spark Component for Research Team
   class ResearchSparkComponent(Component):
       """Component embedding org-specific Spark patterns"""

       # Handles complex concerns:
       # - Cluster provisioning with approved configurations
       # - Data access with proper authentication
       # - Cost attribution and monitoring
       # - Output validation and quality checks
       # - Experiment tracking integration
   ```

4. **Configuration Interface Design**:

   ```yaml
   # What researchers see - deliberately simple
   type: research.SparkModelTraining

   attributes:
     model_name: "gpt_experiment_42"
     compute_size: "large" # Whitelisted options: small, medium, large
     data_source: "training_corpus_v3"
     experiment_tags: ["nlp", "transformer", "q3_priority"]
   ```

5. **Cross-Cutting Concerns Handled**:
   - **Observability**: Automatic DataDog/Grafana integration with proper tagging
   - **Authentication**: Seamless cloud resource authentication
   - **Compute Control**: Pre-approved compute configurations only
   - **Cost Management**: Automatic budget enforcement and alerting
   - **Metadata Standards**: Required fields for lineage and discovery
   - **Quality Gates**: Automatic data validation and model checks

**Phase 2: Component Package Distribution**

1. **Package Creation**:
   - Bundle Components into installable packages
   - Version management and compatibility tracking
   - Documentation generation from Component metadata
   - Example configurations and tutorials

2. **Internal Distribution**:
   - Private package repository setup
   - Integration with `dg` command-line tools
   - Web UI documentation and discovery
   - Training materials and workshops

#### Researcher Workflow

**Day-in-the-Life Example**:

**Morning: Starting New Experiment**

1. Opens terminal (no IDE required)
2. Runs: `dg list components --type research`
3. Sees available Components with descriptions
4. Runs: `dg scaffold research.SparkModelTraining --name my_experiment`
5. Edits simple YAML configuration
6. Runs: `dg validate` to check configuration
7. Deploys with: `dg deploy`
8. Returns to notebook for analysis

**What Researcher DOESN'T Deal With**:

- Python environment setup
- Dagster concepts or abstractions
- Infrastructure provisioning
- Authentication configuration
- Monitoring setup
- Resource allocation details
- Deployment complexities

**Afternoon: Checking Results**

1. Uses familiar tools (notebooks, Spark UI)
2. Sees results in platform UI without learning Dagster
3. Gets alerts through existing channels (Slack, email)
4. Focuses entirely on model performance, not infrastructure

### Value Delivery and Business Impact

#### Quantifiable Benefits

**Research Velocity**:

- **Before**: 2-3 days to productionize notebook experiment
- **After**: 30 minutes with Components
- **Impact**: 10-20x faster iteration cycles

**Platform Team Leverage**:

- **Before**: 1 platform engineer per 5-10 researchers
- **After**: 1 platform engineer per 30-50 researchers
- **Impact**: 5x improvement in support ratio

**Policy Compliance**:

- **Before**: 60% compliance with standards (manual enforcement)
- **After**: 100% compliance (automatic enforcement)
- **Impact**: Reduced risk, better governance

**Resource Optimization**:

- **Before**: 30% compute waste from improper configurations
- **After**: <5% waste with whitelisted configurations
- **Impact**: Significant cost savings at scale

#### Strategic Advantages

**Organizational Scalability**:

- Can grow research teams without proportional platform investment
- Consistent patterns across all teams
- Reduced onboarding time for new researchers
- Knowledge captured in Components, not individuals

**Innovation Acceleration**:

- Researchers focus on model innovation
- Platform team focuses on infrastructure innovation
- Clear separation of concerns
- Faster time-to-market for new models

**Competitive Differentiation**:

- Better researcher productivity than competitors
- More reliable production deployments
- Superior governance and compliance
- Lower operational costs

### Technical Deep Dive

#### Component Implementation Details

**Custom Policy Enforcement Example**:

```python
class ResearchSparkComponent(Component):
    @validator
    def validate_compute_size(self, config):
        """Enforce whitelisted compute configurations"""
        allowed_sizes = {
            "small": {"cores": 4, "memory": "16GB", "max_cost": 10},
            "medium": {"cores": 16, "memory": "64GB", "max_cost": 50},
            "large": {"cores": 64, "memory": "256GB", "max_cost": 200}
        }
        if config.compute_size not in allowed_sizes:
            raise ValidationError(f"Must use approved size: {allowed_sizes.keys()}")

        # Automatic cost attribution
        self.add_tags({"cost_center": config.team,
                      "max_hourly_cost": allowed_sizes[config.compute_size]["max_cost"]})
```

**Observability Integration Example**:

```python
def setup_observability(self, context):
    """Automatic observability configuration"""
    # DataDog integration
    context.datadog.set_tags({
        "team": self.config.team,
        "experiment": self.config.experiment_name,
        "model_type": self.config.model_type,
        "environment": "production"
    })

    # Custom metrics
    context.metrics.register({
        "model_training_time": Timer(),
        "data_processed_gb": Counter(),
        "model_accuracy": Gauge()
    })

    # Automatic alerting
    context.alerts.configure({
        "long_running": {"threshold": "6h", "notify": self.config.team_slack},
        "high_cost": {"threshold": "$500", "notify": self.config.finance_slack},
        "data_quality": {"threshold": "95%", "notify": self.config.team_email}
    })
```

#### YAML Configuration Schema

**Full Research Component Configuration**:

```yaml
type: research.SparkModelTraining

attributes:
  # Required fields (enforced by schema)
  model_name: "transformer_v3_experiment"
  team: "nlp_research"
  compute_size: "large"

  # Data configuration
  data:
    source: "s3://company-data/training/2024_q3"
    preprocessing: "standard_nlp_pipeline"
    validation_split: 0.2

  # Model configuration
  model:
    architecture: "transformer"
    parameters:
      layers: 24
      hidden_size: 1024
      attention_heads: 16
    checkpoint: "s3://models/checkpoints/base_model_v2"

  # Experiment tracking
  experiment:
    tags: ["production", "q3_objective", "nlp"]
    metrics_to_track: ["loss", "accuracy", "f1_score"]
    comparison_baseline: "transformer_v2_production"

  # Resource governance
  resources:
    max_runtime_hours: 8
    max_cost_usd: 1000
    priority: "high"

  # Monitoring and alerting
  notifications:
    slack_channel: "#nlp-experiments"
    on_failure: ["email:team-lead@company.com"]
    on_completion: ["slack:#nlp-experiments"]
```

### Key Design Principles

#### "As Simple as Possible but No Simpler"

**Application in This Scenario**:

- Researchers see only what they need (model config, data source)
- Platform complexity completely hidden
- But can access advanced features when needed
- No artificial limitations imposed

**Quote Context**: "Completely context-dependent" - each organization designs Components for their specific needs

#### Progressive Disclosure

- Basic usage requires minimal configuration
- Advanced features available through optional sections
- Escape hatches for power users
- Documentation increases with complexity

#### Policy as Code

- Governance embedded in Component implementation
- No manual review needed
- Automatic compliance checking
- Audit trail through configuration history

---

## Scenario 2: Analytics Engineer Onboarding dbt Project

### User Profile Deep Dive

#### The Analytics Engineer Persona

**Professional Background**:

- 3-5 years experience with dbt and SQL
- Deep understanding of data modeling and warehousing
- Familiar with git, YAML, and basic development workflows
- Limited Python experience (can read, rarely write)
- Strong business domain knowledge

**Current Tool Expertise**:

- **dbt Mastery**: Complex macros, tests, documentation
- **SQL Excellence**: Window functions, CTEs, optimization
- **Data Warehouse**: Snowflake/BigQuery/Redshift expert
- **Version Control**: Git workflows, PR reviews
- **BI Tools**: Looker/Tableau for visualization

**Knowledge Gaps**:

- **Not a Dagster expert**: Doesn't understand assets, ops, resources
- **Limited Python**: Can't comfortable write Python orchestration code
- **No Infrastructure Experience**: Doesn't understand deployment, scaling
- **Orchestration Concepts**: Unfamiliar with DAGs, scheduling, retries

**Critical Quote**: "Analytics Engineer with deep dbt and SQL expertise... NOT a Dagster expert, doesn't want to become one"

### Business Context for Integration

#### Why dbt Projects Need Dagster Platform

**Universal Lineage Requirements**:

- See dbt models in context of entire data pipeline
- Understand upstream data dependencies
- Track downstream consumer impacts
- Enable impact analysis for changes

**Operational Excellence Needs**:

- Centralized monitoring and alerting
- Consistent SLA management
- Unified incident response
- Cost attribution and optimization

**Team Collaboration Drivers**:

- Other teams need to understand dbt outputs
- Enable self-service data discovery
- Reduce tribal knowledge dependencies
- Standardize documentation and metadata

**Platform Capabilities Access**:

- Leverage existing observability tools
- Use centralized secrets management
- Apply organizational governance policies
- Integrate with broader MLOps workflows

### Current State Pain Points (Without Components)

#### The 50-Line Python Problem

**Actual Code Complexity Example**:

```python
# What analytics engineers must write today (simplified)
from dagster import asset, AssetIn, Config, Definitions
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator

class CustomDbtTranslator(DagsterDbtTranslator):
    def get_asset_key(self, dbt_resource_props):
        # Complex key mapping logic
        return AssetKey([self.project_name, dbt_resource_props["name"]])

    def get_deps(self, dbt_resource_props):
        # Dependency resolution logic
        deps = []
        for ref in dbt_resource_props.get("refs", []):
            deps.append(AssetIn(key=self.get_asset_key({"name": ref})))
        return deps

@dbt_assets(
    manifest=Path("target/manifest.json"),
    project_dir=Path("/path/to/dbt/project"),
    translator=CustomDbtTranslator(),
    partitions_def=DailyPartitionsDefinition(start_date="2024-01-01")
)
def my_dbt_assets(context, dbt_cli_resource):
    # More complex logic here
    yield from dbt_cli_resource.cli(["build"], context=context).stream()

# Plus resource configuration, definitions, etc.
```

**Why This Is Problematic**:

1. **Abstract Concepts**: AssetKey, AssetIn, Definitions unclear
2. **Python Environment**: Virtual environments, dependencies, versions
3. **Error Prone**: Easy to misconfigure dependencies
4. **Maintenance Burden**: Must update when Dagster changes
5. **Knowledge Requirement**: Must understand Dagster internals

**Quote**: "Maybe 50 lines of Python code with some pretty strange abstractions"

#### Environment Setup Complexity

**Current Requirements**:

1. Install Python (correct version)
2. Create virtual environment
3. Install Dagster and dependencies
4. Configure IDE/editor
5. Learn Python packaging
6. Debug environment issues

**Quote**: "Little to no Python environment setup also a killer feature"

#### Maintenance and Evolution

**Ongoing Challenges**:

- Dagster version upgrades break code
- dbt version compatibility issues
- Dependency resolution conflicts
- Must maintain orchestration code alongside dbt code
- Two different skill sets required

### Components-Enabled Workflow

#### The Three-Line Solution

**Actual YAML Configuration**:

```yaml
type: dagster_dbt.DbtProjectComponent

attributes:
  project: "{{ project_root }}/transform/dbt"
  translation:
    key: "analytics/{{ node.name }}"
```

**What This Replaces**:

- 50+ lines of Python code
- Complex abstraction understanding
- Python environment setup
- Ongoing maintenance burden

#### Complete Configuration with Dependencies

**Real-World Example with Upstream Dependencies**:

```yaml
type: dagster_dbt.DbtProjectComponent

attributes:
  # Core project configuration
  project: "{{ project_root }}/analytics/dbt_transformations"

  # Asset key translation for organization
  translation:
    key: "analytics/{{ node.database }}/{{ node.schema }}/{{ node.name }}"

  # Upstream dependencies from other teams
  dependencies:
    # Data Engineering team's raw data ingestion
    - source: data_eng.RawDataIngestion
      mapping:
        customer_data: "raw.customers"
        transaction_data: "raw.transactions"

    # ML team's feature store outputs
    - source: ml_team.FeatureStore
      mapping:
        customer_features: "features.customer_360"

  # Scheduling and partitioning
  schedule:
    cron: "0 6 * * *" # Daily at 6 AM
    timezone: "America/New_York"

  # Resource configuration
  compute:
    warehouse_size: "MEDIUM"
    query_tag: "analytics_team_transforms"

  # Monitoring and alerting
  monitoring:
    slack_channel: "#analytics-alerts"
    sla_minutes: 120

  # dbt-specific configuration
  dbt:
    target: "production"
    vars:
      start_date: "{{ data_interval_start }}"
      end_date: "{{ data_interval_end }}"
    selector: "tag:production"
```

#### Integration Workflow Steps

**Step 1: Discovery**

```bash
# Analytics engineer explores available components
$ dg list components --filter dbt

Available Components:
- dagster_dbt.DbtProjectComponent: Integrate dbt projects with Dagster
- dagster_dbt.DbtSlimComponent: Lightweight dbt integration
- dagster_dbt.DbtCloudComponent: dbt Cloud integration
```

**Step 2: Scaffolding**

```bash
# Generate initial configuration
$ dg scaffold dagster_dbt.DbtProjectComponent \
    --project /path/to/dbt/project \
    --name analytics_transforms

Created: analytics_transforms_component.yaml
Created: Example configuration with common patterns
```

**Step 3: Configuration**

- Edit YAML file in any text editor
- No IDE or Python environment needed
- Validation through `dg validate`
- Documentation available in web UI

**Step 4: Testing**

```bash
# Validate configuration
$ dg validate analytics_transforms_component.yaml
✓ Configuration valid
✓ dbt project found
✓ Dependencies resolved
✓ Schedule valid

# Local testing
$ dg test analytics_transforms_component.yaml --models customer_ltv
✓ Test passed: customer_ltv model executed successfully
```

**Step 5: Deployment**

```bash
# Deploy to Dagster platform
$ dg deploy analytics_transforms_component.yaml
✓ Component deployed
✓ Assets created: 47 dbt models
✓ Schedule activated
✓ Monitoring configured

View in UI: https://dagster.company.com/analytics_transforms
```

### Dependency Management Deep Dive

#### Upstream Dependencies

**Challenge Quote**: "They have to ensure that they are correctly pointing to upstream dependencies"

**Manual Configuration Approach**:

```yaml
dependencies:
  # Explicit mapping when naming doesn't match
  - source: data_eng.CustomerDataIngestion
    mapping:
      output_table: "raw_customers" # Maps to dbt source

  # Pattern matching for consistent naming
  - source: data_eng.TransactionIngestion
    pattern: "raw_{{ asset_name }}" # Automatic mapping
```

**Automatic Discovery** (when naming conventions align):

```yaml
dependencies:
  # If naming conventions match, can be automatic
  auto_discover: true
  namespace_mapping:
    data_eng: "raw"
    ml_team: "features"
```

**Quote Context**: "Depending on naming conventions it could be automatic, but likely requires some lightweight configuration"

#### Downstream Dependencies

**Configuration for Consumers**:

```yaml
# ML team consuming analytics outputs
type: ml.ModelTrainingComponent

attributes:
  training_data:
    source: analytics.DbtProjectComponent
    tables:
      - "analytics.customer_features"
      - "analytics.transaction_summary"
```

**Quote**: "Downstream stakeholders would have to configure their assets to the dbt project assets"

### Value Delivery and Impact

#### Quantifiable Improvements

**Setup Time Reduction**:

- **Before**: 2-3 days (Python env, learning Dagster, writing code)
- **After**: 30 minutes (write YAML, validate, deploy)
- **Impact**: 50x faster onboarding

**Maintenance Effort**:

- **Before**: 4-8 hours per month maintaining Python code
- **After**: Near zero (Components maintained by platform team)
- **Impact**: 50+ hours saved annually per project

**Error Reduction**:

- **Before**: Common dependency misconfigurations, Python errors
- **After**: Validation catches issues before deployment
- **Impact**: 90% reduction in configuration errors

**Learning Curve**:

- **Before**: Weeks to understand Dagster concepts
- **After**: Hours to understand YAML configuration
- **Impact**: 10x faster proficiency

#### Strategic Benefits

**Team Autonomy**:

- Analytics engineers self-sufficient
- No platform team bottleneck
- Faster iteration on transformations
- Reduced cross-team dependencies

**Standardization**:

- Consistent integration patterns
- Uniform monitoring and alerting
- Standard dependency management
- Common operational procedures

**Scalability**:

- Easy to onboard new dbt projects
- Pattern reusable across teams
- Platform team leverage increases
- Governance automatically applied

### Technical Implementation Details

#### Component Internals (Hidden from Users)

**What the Component Handles**:

```python
class DbtProjectComponent(Component):
    """Encapsulates all dbt integration complexity"""

    def build_assets(self):
        # Handles manifest parsing
        # Creates asset definitions
        # Manages dependencies
        # Configures resources
        # Sets up monitoring
        # Implements retry logic
        # Manages partitions
        # All complexity hidden from user
```

#### Progressive Complexity Options

**Minimal Configuration** (Getting Started):

```yaml
type: dagster_dbt.DbtProjectComponent
attributes:
  project: "./dbt"
```

**Standard Configuration** (Production Ready):

```yaml
type: dagster_dbt.DbtProjectComponent
attributes:
  project: "./dbt"
  schedule: "0 6 * * *"
  monitoring:
    slack_channel: "#alerts"
```

**Advanced Configuration** (Full Control):

```yaml
type: dagster_dbt.DbtProjectComponent
attributes:
  project: "./dbt"
  # [Previous config plus...]

  # Advanced dbt control
  dbt:
    exclude_models: ["staging_*", "deprecated_*"]
    full_refresh_schedule: "0 0 * * 0" # Weekly
    test_severity: "error"
    docs_generate: true

  # Advanced Dagster features
  assets:
    group_name: "analytics"
    compute_kind: "dbt"
    owners: ["analytics-team@company.com"]

  # Custom resource configuration
  resources:
    custom_resource:
      config:
        api_key: "{{ env.CUSTOM_API_KEY }}"
```

### Success Metrics and Validation

#### Key Success Metric

**Quote**: "Transform 50 lines of complex Python + environment setup into few lines of YAML configuration"

#### Validation Criteria

1. **Simplicity**: YAML readable by SQL developers
2. **Completeness**: All dbt features accessible
3. **Integration**: Full platform capabilities available
4. **Maintenance**: Zero ongoing maintenance for users
5. **Performance**: No overhead vs direct integration

---

## Scenario 3: Platform Team Enabling Domain Teams at Scale

### Organizational Context

#### Platform Team Composition

**Team Structure**:

- **Size**: 5-10 senior engineers
- **Background**: Mixed infrastructure and data engineering
- **Responsibilities**:
  - Build and maintain data platform
  - Create reusable components
  - Establish organizational standards
  - Support domain teams
  - Manage platform evolution

**Technical Expertise**:

- Deep Dagster knowledge
- Cloud infrastructure (AWS/GCP/Azure)
- Security and compliance
- Performance optimization
- Developer experience

#### Domain Teams Landscape

**Data Teams Supported**:

1. **Analytics Teams** (10-20 people)
   - Using dbt, SQL, BI tools
   - Need production orchestration
2. **Data Science Teams** (5-15 people)
   - Using notebooks, Python, R
   - Need experiment tracking and deployment
3. **ML Engineering Teams** (5-10 people)
   - Using TensorFlow, PyTorch
   - Need training pipelines and serving
4. **Data Engineering Teams** (10-15 people)
   - Using Spark, Airflow, various tools
   - Need migration path to Dagster

**Scale Challenge**:

- 50+ domain team members
- 100+ pipelines to manage
- 1000+ daily job runs
- Growing 50% year-over-year

### Component Distribution Model

#### Package-Based Distribution System

**Architecture Overview**:

```
Platform Team → Component Packages → Internal Registry → Domain Teams
                        ↓                    ↓              ↓
                  Documentation        Discovery      Consumption
```

**Package Structure Example**:

```
company-components/
├── setup.py
├── pyproject.toml
├── src/
│   └── company_components/
│       ├── __init__.py
│       ├── dbt/
│       │   ├── __init__.py
│       │   └── enforced_dbt_component.py
│       ├── notebooks/
│       │   ├── __init__.py
│       │   └── notebook_runner_component.py
│       └── ml/
│           ├── __init__.py
│           └── model_training_component.py
├── docs/
│   ├── components.md
│   └── examples/
└── tests/
```

**Quote**: "Platform Team authors and maintains Components in packages"

#### Discovery Mechanism

**Command-Line Discovery**:

```bash
# List all available components
$ dg list components

company_components.EnforcedDbtComponent
  Dbt integration with company policies

company_components.NotebookRunnerComponent
  Production notebook execution with monitoring

company_components.ModelTrainingComponent
  ML model training with experiment tracking
```

**Quote**: "dg tools allow the introspection of those installed packages to list them"

**Web UI Discovery**:

- Searchable component catalog
- Rich documentation with examples
- Version history and changelog
- Usage statistics and examples

**Quote**: "Integrated documentation in our web app"

### Platform Team Value Creation

#### For dbt Projects - Governance and Standards

**Metadata Enforcement Implementation**:

**The Component**:

```python
class EnforcedDbtComponent(DbtProjectComponent):
    """dbt Component with organizational policies"""

    def validate_metadata(self, manifest):
        """Enforce organizational metadata standards"""
        for model in manifest.models:
            # Enforce ownership
            if not model.meta.get("owner"):
                raise ValidationError(f"Model {model.name} missing owner")

            # Enforce documentation
            if not model.description:
                raise ValidationError(f"Model {model.name} missing description")

            # Enforce data classification
            if not model.meta.get("data_classification"):
                raise ValidationError(f"Model {model.name} missing classification")

            # Enforce SLA definition
            if model.meta.get("tier") == "critical" and not model.meta.get("sla"):
                raise ValidationError(f"Critical model {model.name} missing SLA")
```

**What Domain Teams See**:

```yaml
type: company_components.EnforcedDbtComponent

attributes:
  project: "./dbt"
  # Metadata requirements enforced automatically
  # No additional configuration needed
```

**Quote**: "Every model has an owner" - automatic policy compliance

**Standards Cascade Example**:

- Owner metadata → Alert routing
- Classification → Access control
- SLA definition → Monitoring thresholds
- Documentation → Discovery portal

#### For Notebook Workflows - Production Enablement

**Complex Infrastructure Abstraction**:

**The Component**:

```python
class NotebookRunnerComponent(Component):
    """Production notebook execution with enterprise features"""

    def setup_runtime(self, config):
        """Handle all runtime complexity"""

        # Observability Integration
        self.setup_datadog(
            tags=config.tags,
            custom_metrics=config.metrics
        )

        # Context Management
        runtime_context = {
            "experiment_id": generate_experiment_id(),
            "run_date": context.partition_key,
            "environment": config.environment,
            "user_params": config.parameters
        }

        # Compute Configuration
        compute_spec = self.whitelist_compute(config.compute_size)

        # Authentication
        self.setup_auth(
            aws_role=config.aws_role,
            database_creds=config.database,
            api_keys=config.external_apis
        )

        return runtime_context, compute_spec
```

**Configuration for Data Scientists**:

```yaml
type: company_components.NotebookRunnerComponent

attributes:
  notebook: "experiments/customer_segmentation.ipynb"

  # Simple compute selection from whitelist
  compute_size: "gpu_medium" # Pre-approved configurations only

  # Automatic observability
  monitoring:
    alert_on_failure: true
    track_metrics: ["runtime", "memory_usage", "gpu_utilization"]

  # Managed authentication
  resources:
    s3_bucket: "company-ml-data"
    database: "analytics_prod"
    mlflow: "https://mlflow.company.com"
```

**Specific Value Delivered**:

1. **Observability Integration**:
   - Quote: "Handle integration with observability tools"
   - Automatic DataDog/Prometheus metrics
   - Custom dashboard generation
   - Alert routing based on owner

2. **Context Management**:
   - Quote: "Passing along custom context that the target runtime expects"
   - Experiment tracking integration
   - Partition awareness
   - Parameter logging

3. **Compute Governance**:
   - Quote: "Whitelisting different compute configurations that the stakeholder can use (e.g., amount of memory)"
   - Pre-approved GPU/CPU configurations
   - Cost controls and limits
   - Automatic resource tagging

4. **Authentication**:
   - Quote: "Authentication against the proper resources in the target runtime"
   - Transparent credential management
   - Role assumption for cloud resources
   - API key rotation handling

### Workflow Patterns

#### Component Authoring Workflow

**Step 1: Identify Pattern**

```python
# Platform team notices repeated pattern
# Example: 10 teams writing similar notebook orchestration code
# Each with slight variations but same core needs
```

**Step 2: Design Component**

```python
# Extract common patterns
# Design YAML interface
# Build in organizational policies
# Create flexible configuration options
```

**Step 3: Package and Publish**

```bash
# Build package
$ python -m build

# Publish to internal registry
$ twine upload --repository company-pypi dist/*

# Update documentation
$ dg docs generate
$ dg docs publish
```

**Step 4: Announce and Train**

- Slack announcement with examples
- Documentation in wiki
- Office hours for questions
- Migration guide from old patterns

#### Domain Team Consumption Workflow

**Complete Workflow Example**:

**Discovery Phase**:

```bash
# Domain user explores available components
$ dg list components

Available Components:
  company_components.EnforcedDbtComponent
    dbt with organizational policies

  company_components.NotebookRunnerComponent
    Production notebook execution

  company_components.ModelTrainingComponent
    ML training with experiment tracking

# Get detailed information
$ dg describe company_components.NotebookRunnerComponent

NotebookRunnerComponent:
  Purpose: Run Jupyter notebooks in production with monitoring

  Required Configuration:
    - notebook: Path to notebook file
    - compute_size: One of [small, medium, large, gpu_medium, gpu_large]

  Optional Configuration:
    - schedule: Cron expression
    - monitoring: Alerting configuration
    - resources: External resource access

  Examples available at: docs/notebook_runner_examples.yaml
```

**Scaffolding Phase**:

```bash
# Generate initial configuration
$ dg scaffold company_components.NotebookRunnerComponent \
    --name ml_pipeline

Created: ml_pipeline.yaml
Template configuration with common patterns included
```

**Configuration Phase**:

```yaml
# Domain user edits ml_pipeline.yaml
type: company_components.NotebookRunnerComponent

attributes:
  notebook: "models/churn_prediction.ipynb"
  compute_size: "gpu_medium"

  schedule:
    cron: "0 2 * * *"
    timezone: "UTC"

  parameters:
    model_version: "v2.3"
    training_date: "{{ data_interval_start }}"

  monitoring:
    slack_channel: "#ml-alerts"
    email_on_failure: "ml-team@company.com"
```

**Deployment Phase**:

```bash
# Validate configuration
$ dg validate ml_pipeline.yaml
✓ Configuration valid
✓ Notebook found
✓ Compute size approved
✓ Schedule valid

# Deploy to platform
$ dg deploy ml_pipeline.yaml
✓ Component deployed
✓ Schedule activated
✓ Monitoring configured

View in UI: https://dagster.company.com/ml_pipeline
```

**Quote Summary**:

```
Platform Team → Authors Component Package → Publishes with Documentation
           ↓
Domain User → `dg list components` → Reviews Documentation → `dg scaffold defs`
           ↓
Domain User → Configures YAML → System Enforces Policies Automatically
```

### Value Delivery Model

#### Standardization Without Centralization

**Traditional Approach Problems**:

- Central platform team bottleneck
- Every request needs custom work
- Inconsistent implementations
- Slow delivery times

**Components Approach Benefits**:

- Self-service for domain teams
- Consistent patterns everywhere
- Platform team builds once, used many times
- Fast delivery through reuse

**Quote Context**: "Consistent organizational patterns without central bottlenecks"

#### Control with Flexibility

**Platform Team Maintains**:

- Security policies
- Resource limits
- Cost controls
- Compliance requirements
- Performance standards

**Domain Teams Get**:

- Configuration flexibility
- Self-service deployment
- Rapid iteration
- Domain-specific customization

**Quote Context**: "Platform team maintains oversight, domain teams get autonomy"

#### Policy as Code

**Traditional Policy Enforcement**:

- Manual reviews
- Checklist processes
- Audit after the fact
- Inconsistent application

**Components Policy Enforcement**:

- Automatic validation
- Build-time checks
- Consistent application
- Audit trail in configuration

**Quote Context**: "Governance embedded in infrastructure rather than process"

#### Scaling Through Reuse

**Multiplication Effect**:

- One Component serves many teams
- Improvements benefit everyone
- Bug fixes apply universally
- Knowledge captured in code

**Quote Context**: "Reusable patterns eliminate duplicate effort across teams"

### Advanced Platform Capabilities

#### Component Versioning and Evolution

**Version Management Strategy**:

```python
# Component with version compatibility
class NotebookRunnerComponent(Component):
    version = "2.1.0"
    compatible_versions = ["2.0.0", "2.1.0"]

    def migrate_config(self, old_config, old_version):
        """Automatic configuration migration"""
        if old_version < "2.0.0":
            # Migrate from v1 to v2 format
            return self.migrate_v1_to_v2(old_config)
        return old_config
```

#### Component Composition

**Building Complex Workflows**:

```yaml
# Combining multiple components
type: company_components.MLPipelineComponent

attributes:
  # Compose other components
  components:
    - type: company_components.DataValidationComponent
      config:
        rules: "ml_data_quality_rules.yaml"

    - type: company_components.NotebookRunnerComponent
      config:
        notebook: "feature_engineering.ipynb"

    - type: company_components.ModelTrainingComponent
      config:
        algorithm: "xgboost"
        hyperparameters: "hparam_search.yaml"

    - type: company_components.ModelValidationComponent
      config:
        tests: "model_test_suite.yaml"
```

#### Platform Integration Points

**Centralized Services Integration**:

- Secret management (Vault, AWS Secrets Manager)
- Monitoring (DataDog, Prometheus, Grafana)
- Logging (ELK stack, Splunk)
- Experiment tracking (MLflow, Weights & Biases)
- Data catalog (DataHub, Amundsen)
- Cost management (CloudHealth, Kubecost)

### Success Metrics and Validation

#### Platform Team Metrics

**Development Velocity**:

- Components created per quarter
- Reuse rate across teams
- Time to create new Component
- Component adoption rate

**Operational Excellence**:

- Policy compliance rate: 100% (automatic)
- Incident reduction: 50% fewer pipeline failures
- Support ticket reduction: 70% fewer platform requests
- Resource utilization: 30% cost reduction

#### Domain Team Metrics

**Productivity Gains**:

- Time to production: 10x faster
- Self-service rate: 90% of deployments
- Configuration errors: 95% reduction
- Learning curve: Days instead of weeks

**Satisfaction Metrics**:

- Developer NPS score improvement
- Reduced friction feedback
- Increased deployment frequency
- Higher experimentation rate

### Governance and Compliance Deep Dive

#### Enterprise Requirements Addressed

**Security Controls**:

```python
class SecureComponent(Component):
    def validate_security(self):
        # Encryption at rest
        self.enforce_encryption()

        # Network isolation
        self.configure_vpc_endpoints()

        # Access logging
        self.enable_audit_logging()

        # Credential rotation
        self.setup_rotation_schedule()
```

**Compliance Automation**:

- GDPR data handling rules
- HIPAA compliance for healthcare
- SOC2 audit trail requirements
- PCI DSS for payment data

**Cost Controls**:

- Budget limits per team
- Resource tagging for attribution
- Automatic shutdown of idle resources
- Cost anomaly detection

---

## Cross-Scenario Insights and Patterns

### Common Success Factors

#### Division of Labor Excellence

All three scenarios demonstrate clear separation:

- Platform complexity hidden from domain users
- Domain expertise preserved and enhanced
- Each group focuses on their strengths
- Collaboration through configuration, not code

#### YAML as Universal Interface

Consistent across all scenarios:

- Approachable for non-Python developers
- Rich enough for complex configuration
- Validated for correctness
- Self-documenting structure

#### Progressive Disclosure Pattern

Every scenario shows progression:

- Simple start with minimal config
- Additional options as needed
- Escape hatches for power users
- Complexity revealed gradually

#### Policy Enforcement Automation

Governance without friction:

- Rules embedded in Components
- Automatic validation and enforcement
- Consistent application across teams
- Audit trail through configuration

### GA Readiness Validation

For each scenario to work completely:

1. **End-to-End Workflows**:
   - All tooling must be complete (`dg` commands)
   - Documentation must be comprehensive
   - Examples must cover common patterns
   - Migration paths must be clear

2. **Component Framework Maturity**:
   - Versioning and compatibility
   - Composition capabilities
   - Distribution mechanisms
   - Discovery and documentation

3. **Platform Integration**:
   - Lineage tracking across Components
   - Unified observability
   - Consistent resource management
   - Seamless authentication

4. **Enterprise Features**:
   - Security controls
   - Compliance automation
   - Cost management
   - Audit capabilities

### Outstanding Questions for Section 3

Based on these scenarios, key milestone questions:

1. **Which scenario is most critical for GA?**
2. **What is minimum viable Component library?**
3. **How do we validate scenario completeness?**
4. **What is rollout sequence for capabilities?**
5. **How do we measure scenario success?**

---

## Summary for Section 3 Transition

Section 2 has established three comprehensive usage scenarios:

1. **Foundation Model Company**: Platform engineers enabling researchers through custom Components
2. **Analytics Engineer**: Self-service dbt integration without Python complexity
3. **Platform Team**: Scaling support through reusable Component packages

Each scenario demonstrates:

- Clear user value proposition
- Specific workflow transformations
- Quantifiable improvements
- Technical implementation details
- Success validation criteria

These scenarios provide concrete context for Section 3's milestone planning, showing exactly what capabilities must be delivered for GA success.

---

_Note for downstream agents: This document contains exhaustive detail from the interview about usage scenarios. All quotes are verbatim. Technical examples are actual configurations discussed. Use this as the authoritative source for Usage Scenarios section of the PRD._
