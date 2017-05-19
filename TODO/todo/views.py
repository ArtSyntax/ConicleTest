from django.contrib.auth.models import User
from rest_framework import generics
from todo.models import *
from todo.serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    '''
    ## GET 
    <http://127.0.0.1:8000/todo/todo/>
    ### result you will get
    ```{
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "subject": "test2",
                "detail": "detail2",
                "status": "D"
            },
            {
                "id": 3,
                "subject": "test3",
                "detail": "detail3",
                "status": "P"
            }
        ]
    }```

    ## POST 
    <http://127.0.0.1:8000/todo/todo/>
    ### data you must post
    ```{
        "subject": "Title",
        "detail": "Description",
        "status": "P"
    }```
    '''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    ## PUT 
    <http://127.0.0.1:8000/todo/todo/<pk\>> (pk is item id)
    ### data you must put to update
    ```{
        "subject": "Title",
        "detail": "Description",
        "status": "D"
    }```

    ## DELETE 
    <http://127.0.0.1:8000/todo/todo/<pk\>>
    
    '''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer