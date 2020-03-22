from django.shortcuts import render

# Create your views here.

from django.http import Http404
#импортирует метод обработки ситуации, когда нет необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from project_first_app.models import Person #импортирует таблицу Poll из модели данных, где polls - название приложения
def detail(request, poll_id):
    print(poll_id)
    try: #метод try-except - обработчик исключений
        p = Person.objects.get(pk=poll_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Person.DoesNotExist:
        raise Http404("Person does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'project_first_app/main.html', {'person': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"