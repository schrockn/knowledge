# Dagster Components - Key Messaging References

## Core Value Propositions (from Roadshow)

### Primary Problem Statement

**"The challenge - Data & AI teams today"**

- **Siloed Teams**: ML engineers, data engineers, and platform teams speak different languages while operating in the same platform
- **Pipeline Chaos**: Lack of standards makes pipelines hard to maintain and understand
- **Accessibility**: Stakeholders and new team members search through unorganized/undocumented projects

### The Vision

**"What if AI and data teams could collaborate on a shared platform using their domain-specific tools of choice"**

**Data scientists**: Onboard new data sets and productionize analysis with simple YAML files, reuse battle-tested pipelines
**Machine learning engineers**: Provide guardrails, add validations, and enable team members
**Platform engineers**: [Enable the above through Components framework]

## Core Product Messaging

### "Introducing Dagster Components"

1. **YAML interfaces and scaffolding** - Enable non-technical (or technical) stakeholders to easily build and configure pipelines without being a Dagster expert
2. **Reusable patterns** - Build once and re-use everywhere, while enforcing best practices
3. **Built-in guardrails** - Enable platform owners to ensure quality and compliance, with guardrails that support AI-native dev workflows

### "Constraints that Enable Creativity"

**Why YAML matters for AI teams:**

- **Enforces Best Practices**: Can't skip error handling or monitoring
- **Enables AI Workflows**: LLMs can generate valid pipeline configs
- **Reduces Errors**: Schema validation catches issues before runtime
- **Democratizes Access**: Data scientists can modify pipelines without Python expertise

### Key Differentiators

- **AI-ready**: Well thought out structure makes LLM-based developer workflows much more efficient
- **Documentation as-code**: Automatically presented through the Dagster UI
- **Customizable scaffolding**: Dynamically populated YAML, generate tool-specific files
- **Advanced templating**: Injectable context and introspectible metadata
- **Easy to understand error messaging**: Clear validation with context

## Developer Experience Advantages

- **dg command-line tool**: Improved local developer experience
- **Elegant Python framework**: Easy to wrap existing pipelines or develop new ones
- **Tight integration**: Automatic documentation in UI, polished stakeholder experience
- **Component marketplace**: Share and discover components

## Future Vision

- **MCP server(s)**: AI tooling integration
- **AI scaffolding**: Context awareness (e.g., error logs)
- **AI summaries**: For failures and operations
- **Expanding Component marketplace**: Community ecosystem

## Technical Flow (Demo Flow)

1. `dg scaffold component` - Create new component
2. Adapt existing script/pipeline code
3. `dg scaffold defs` - Create definition instance
4. Configure YAML with schema validation
5. `dg check yaml` / `dg check defs` - Validation
6. `dg dev` - Local development with UI
7. Deploy with clear error messaging and documentation

## Key Personas Addressed

- **Medium-Code Practitioners**: Domain experts (analytics engineers, data scientists) who use real programming languages but don't want to become platform experts
- **Data Scientists**: Move beyond notebooks to production ML systems
- **Analytics Engineers**: Bridge data engineering and analytics using domain tools like dbt
- **Platform Engineers**: Create reusable abstractions and reduce cognitive load for domain experts
- **Infrastructure Engineers**: Build platforms that enable medium-code development

## Additional Context from Blog Post

- **"Low-Code Convenience with High-Code Power"**: Configuration-based development with programmatic control when needed
- **AI-Ready Design**: Built for AI-assisted development workflows
- **Unified CLI Experience**: Consistent command-line interface
- **Preview Status Focus**: Currently seeking user feedback to shape future development

## Medium-Code Definition (Key Context)

- **Turing Complete Languages**: Uses real programming languages (Python, SQL, JavaScript)
- **Version Control Integration**: Follows software development lifecycle practices
- **Production Ready**: Runs in production environments
- **Infrastructure Abstraction**: Abstracts away complex infrastructure concerns
- **Domain-Specific Tools**: Enables mission-critical software without full-stack expertise

## AI Integration Specifics

- **Context Engineering**: Structured data and metadata essential for effective model building
- **Foundation Model Training**: Real-world usage example (Poolside uses Dagster for data ingest to model training)
- **Schema-Rich**: Constrained, metadata-rich codegen target
- **Less Context Required**: Easier for LLMs to generate compared to competitors
