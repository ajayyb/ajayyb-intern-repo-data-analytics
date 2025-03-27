Static Analysis Checks in CI/CD #50

What is the purpose of CI/CD?
- Automate integration (detects issues early)
- Consistency
- Quicker and more accurate deliver of software changes

How does automating style checks improve project quality?
- Ensures consitent code style across the team
- Makes code more readable as it is all formatted into the same format
- 

What are some challenges with enforcing checks in CI/CD?
- Performance can be slowed as running multiple tests through the pipeline (if not done well) can be slow
- In legacy codebases, changes may not be welcome


How do CI/CD pipelines differ between small projects and large teams?
- Small Projects:
    - Less use of pipeline, as it can be easy to manage as there are not many contributors
    - More simple pipelines

- Large Projects:
    - Much more complex pipelines (multiple stages)
    - Frequent automated deployments 