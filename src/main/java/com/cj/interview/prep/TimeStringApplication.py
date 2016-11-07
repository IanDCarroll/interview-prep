
'''
## Goal
- During the coding screen, the goal is for us to experience what it is like to code with you.
- In preparation for the screen, we want you to have an idea of the type of coding we do.
- If you feel you are rusty, or this sample takes you more than an hour, you are probably not ready to interview with us.

## Recommendations
- Do this in the language you are most comfortable with, anything https://coderpad.io/ supports will be fine
- Test drive your code, we do test driven design here, so you will want to make sure this is a style you can tolerate
- Standard libraries only
- Write your own test functions (no need for a whole test framework, focus on the parts you need for this exercise)

## Practice requirements
- no one is going to look at your results here, this is so you can have an idea of what the coding exercise might be like
- Prove that you can correctly implement a function where
    - Input: a bunch of times, minutes and seconds, formatted as a single string like: "12:32 34:01 15:23 9:27 55:22 25:56"
    - Output: the sum of the times, hours, minutes, and seconds, formatted as a single string like: "2:32:41"

## For More Information
- Do some research on "test driven development," focusing on how this style of testing can change your design
'''


class TimeStringApplication(object):
    def raw_second_converter(self, raw_seconds):
        seconds_in_a_minute = 60
        seconds_in_an_hour = 3600
        seconds = str(raw_seconds % 60)
        minutes = str(raw_seconds / seconds_in_a_minute % 60)
        hours = str(raw_seconds / seconds_in_an_hour % 60)
        temporal_conversion = hours + ":" + minutes + ":" + seconds
        return temporal_conversion


    def flux_capacitor(self, time_string):

        time_array = time_string.split(' ')
        raw_seconds = 0
        for i in range(0, len(time_array)):
            time_unit = time_array[i].split(':')
            raw_seconds += int(time_unit[1])
            raw_seconds += int(time_unit[0]) * 60
        return self.raw_second_converter(raw_seconds)
