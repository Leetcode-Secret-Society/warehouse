class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        people_on_time = collections.defaultdict(list)
        for i in range(len(arrival)):
            people_on_time[arrival[i]].append(i)
        # print(people_on_time)
        current_time = 0
        current_in = deque()
        current_out = deque()
        # current_in = list() #using list and pop(0) would be a lot slower
        # current_out = list()
        is_last_exited = True
        result = [None] * len(arrival)

        def handle_people(current_in, current_out, result, current_time, is_last_exited) -> (bool,bool) :
            is_door_used = False
            if is_last_exited and current_out:
                result[current_out.popleft()] = current_time
                is_door_used = True
            elif not is_last_exited and current_in:
                result[current_in.popleft()] = current_time
                is_door_used = True
            elif current_out:
                result[current_out.popleft()] = current_time
                is_door_used = True
                is_last_exited = True
            elif current_in:
                result[current_in.popleft()] = current_time
                is_door_used = True
                is_last_exited = False
            # print(f"hp: {result=} {current_out=} {current_in=} {current_time=}")
            return (is_last_exited, is_door_used)

        # Your existing code
        for time, people in people_on_time.items():
            while current_time < time:     
                is_last_exited, is_door_used = handle_people(current_in, current_out, result, current_time, is_last_exited)
                if not is_door_used:
                    is_last_exited = True
                current_time += 1

            for person in people:
                if state[person] == 0:
                    current_in.append(person)
                else:
                    current_out.append(person)
            # print(f"pot: {current_out=} {current_in=} {time=}")
                

        # print("remaining")
        # Remaining people
        while current_in or current_out:
            is_last_exited, is_door_used = handle_people(current_in, current_out, result, current_time, is_last_exited)
            if not is_door_used:
                is_last_exited = True
            current_time += 1
        
        # print((current_in, current_out))
        return result
