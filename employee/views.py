from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee.forms import empform, leaveform, holidayform
from django.contrib import messages


def emp(Request):
    form = empform()
    if Request.method == 'POST':
       form = empform(Request.POST)
       if form.is_valid():
           form.save(commit=True)
           return redirect('login')
       else:
           print("Error form Invalid")
    return render(Request, 'employee/emp.html', {'form': form})


def leave(Request):
    form = leaveform()
    if Request.method == "POST":
        form = leaveform(Request.POST)
        startdate = Request.POST['startdate']
        enddate = Request.POST['enddate']
        if enddate >= startdate:
            print(startdate)
            print(type(startdate))
            from datetime import datetime
            # import holidays
            import datetime

          # Startdate 2023-03-11
            yyyy = int(startdate[0:4])
            mm = int(startdate[5:7])
            dd = int(startdate[-2:])
          # enddate
            yyyy_e = int(enddate[0:4])
            mm_e = int(enddate[5:7])
            dd_e = int(enddate[-2:])

            start = datetime.date(yyyy, mm, dd)
            end = datetime.date(yyyy_e, mm_e, dd_e)

            daydiff = end.weekday() - start.weekday()

            days = ((end - start).days - daydiff) / 7 * 5 + min(daydiff, 5) - (max(end.weekday() - 4, 0) % 5)

            print(start,'********',days,'********',end)

            # ind_holidays = holidays.India()
            # x = datetime(yyyy, mm, dd, 00, 00, 00, 0000)
            # print('^^^^^^^^^^^^^^^^', x, '^^^^^^^^^^^^^^^^')
            form.save(commit=True)
            if form.is_valid():
                form.save(commit=True)
                return render(Request, 'employee/display.html', context={'days': days})

            # return redirect('leave')
            else:
                print("Error form invalid")



                # return HttpResponse("<h1>Leave applied successfully</h1>")
        else:
            messages.info(Request, "Please enter the correct date")
            return redirect('leave')
    return render(Request, "employee/emp_leave.html", {'form': form})



def holiday(Request):
    form = holidayform()
    if Request.method == 'POST':
       form = holidayform(Request.POST)
       if form.is_valid():
           form.save(commit=True)
           return HttpResponse("<h1> Record Inserted Successfully</h1>")
       else:
           print("Error form Invalid")
    return render(Request, 'employee/holiday.html', {'form': form})
