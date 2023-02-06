from frat.frat import FRAT, takeAttendance

if __name__ == '__main__':
    frat = FRAT(callback = takeAttendance)
    frat.encodeFaces()
    frat.start()