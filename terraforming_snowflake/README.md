# terraforming_snowflake
Terraform is an open-source Infrastructure as Code (IaC) tool created by HashiCorp. It is a declarative Infrastructure as Code tool, meaning instead of writing step-by-step imperative instructions like with SQL, JavaScript or Python, you can declare what you want using a YAML like syntax. Terraform is also stateful, meaning it keeps track of your current state, and compares it with your desired state. A reconcilation process between the two states generates an plan that Terraform can execute to create new resources, or update/delete existing resources. This plan is implemented as an acyclic graph, and is what allows Terraform to understand and handle dependencies between resources. Using Terraform is a great way to manage account level Snowflake resources like Warehouses, Databases, Schemas, Tables, and Roles/Grants, among many other use cases

### git commands
```$ git init```

```$ git add README.md```

```$ git commit -m "first commit"```

```$ git branch -M main```

```$ git remote add origin git@github.com:YOUR_GITHUB_USERNAME/terraforming_snowflake.git```

```$ git push -u origin main```


```printenv``` - displays environment variables in linux