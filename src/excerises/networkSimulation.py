
from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])



class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        arrived_time = request.arrived_at
        time_process = request.time_to_process

        while self.finish_time and self.finish_time[0] <= arrived_time:
            self.finish_time.pop(0)

        if len(self.finish_time) >= self.size:
            return Response(True, -1)

        start_time = max(arrived_time, self.finish_time[-1] if self.finish_time else 0)
        finish_time = start_time + time_process

        self.finish_time.append(finish_time)
        return Response(False, start_time)

        

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

