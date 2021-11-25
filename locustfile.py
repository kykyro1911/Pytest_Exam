from locust import HttpUser, TaskSet, task, constant
import os, json

class WebsiteTasks(TaskSet):
    @task()
    def re_get(self):
        resp = self.client.get("people/1/")
        json_re = json.loads(resp.text)
        # http status是否為200
        assert resp.status_code == 200, "HTTP response is " + resp.status_code
        # vehicles size >= 1
        assert len(json_re['vehicles']) >= 1, json_re['name'] + "'s vehicles amount is not less than or equal to 1"
        

class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    host = 'https://swapi.dev/api/'
    wait_time = constant(1)
    # stop_timeout = 10


if __name__ == "__main__":
    os.system('locust -f ' + __file__ +  ' --autostart -u 10 -r 10 -t 10s --autoquit 1')
