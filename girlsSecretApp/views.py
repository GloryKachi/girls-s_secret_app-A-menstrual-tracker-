from django.shortcuts import render
from datetime import datetime, timedelta, date


def details(request):
    if request.method == 'POST':
        period_date = datetime.strptime(request.POST['period_date'], '%Y-%m-%d').date()
        cycle_length = int(request.POST['cycle_length'])
        next_period_date = period_date + timedelta(days=cycle_length)
        next_period_day = next_period_date.strftime('%A')

        cycle_days = round(cycle_length / 2)
        ovulation_date = period_date + timedelta(days=cycle_days)
        result = ovulation_date.strftime('%B %d, %Y')

        unsafe_days = next_period_date + timedelta(days=cycle_days)
        next_unsafe_day = ovulation_date.strftime('%B %d, %Y')
        next_twelve = []
        unsafe_days = []

        for i in range(12):
            next_period_date = period_date + timedelta(days=cycle_length)
            new_ovulation_date = next_period_date + timedelta(days=cycle_days)
            unsafe_days = []
            for days in range(0, 3):
                ovulation_dates = new_ovulation_date - timedelta(days=days + 1)
                unsafe_days.append(ovulation_dates)

            unsafe_days.reverse()
            for days in range(0, 3):
                ovulation_dates = new_ovulation_date + timedelta(days=days + 1)
                unsafe_days.append(ovulation_dates)
                sorted(unsafe_days)
            next_twelve.append([next_period_date, new_ovulation_date, unsafe_days])
            period_date = next_period_date

        return render(request, 'details.html', {
            "period_date": period_date,
            "next_period_date": next_period_date,
            "next_period_day": next_period_day,
            "ovulation_date": ovulation_date,
            "next_twelve": next_twelve,
            # "unsafe_days": unsafe_days,
        })
    return render(request, 'details.html')
