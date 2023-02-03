from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_pokemons(self):
        for pokemon in range(20):
            self.client.get("/battle/" + str(pokemon) + "/" + str(pokemon + 1))