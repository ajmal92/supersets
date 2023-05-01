# supersets

- dashboards should be placed in `config` folder
- loop through all the folders iin `config` and create a archive folder in a temperory director
- Use superset dashboard api to import dashboards and pass the .zip version of dashboard
- The pipeline accepts three arguments `base_url`, `username`, `password'
- This can be used to deploy the dashboards in different environments by passing appropriate `base_url`, `username`, `password`.
