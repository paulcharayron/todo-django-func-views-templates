from django.shortcuts import render


def errorPage(request, err_msg):
    return render(
        request,
        "error.html",
        {
            "err_msg": err_msg,
        },
    )
