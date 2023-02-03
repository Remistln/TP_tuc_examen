from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_pokemons(self):
        for pokemon in range(1, 20):
            self.client.get("/pokemons/battle/" + str(pokemon) + "/" + str(pokemon + 1))

    @task
    def view_stats(self):
        self.client.get("/pokemon/")
