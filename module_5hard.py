# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему
# IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

from time import sleep

# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __str__(self):
        return f'{self.nickname}'

# Каждый объект класса Video должен обладать следующими атрибутами и методами: Атрибуты: title(заголовок, строка),
# duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по
# возрасту, bool (False по умолчанию))

class Video:
    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


# Каждый объект класса UrTube должен обладать следующими атрибутами и методами: Атрибуты: users(список объектов
# User), videos(список объектов Video), current_user(текущий пользователь, User) Метод log_in, который принимает на
# вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой
# пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки,
# а сравнивается по хэшу. Метод register, который принимает три аргумента: nickname, password, age, и добавляет
# пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
# "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически. Метод log_out для
# сброса текущего пользователя на None. Метод add, который принимает неограниченное кол-во объектов класса Video и
# все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
# слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр). Метод
# watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не
# воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время
# просмотра данного видео сбрасывается. Для метода watch_video так же учитывайте следующие особенности: Для паузы
# между выводами секунд воспроизведения можно использовать функцию sleep из модуля time. Воспроизводить видео можно
# только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт,
# чтобы смотреть видео" Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
# т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу" После
# воспроизведения нужно выводить: "Конец видео"


class UrTube:
    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        return self == other

    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname, password):
        for find_user in self.users:
            if find_user.nickname == nickname and hash(find_user.password) == hash(password):
                self.current_user = find_user
        return self.current_user

    def register(self, nickname, password, age):
        user_ = User(nickname, password, age)

        if not self.users:
            self.users.append(user_)
            self.current_user = user_
        else:
            for i in self.users:
                if i.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    break
                else:
                    self.users.append(user_)
                    self.current_user = user_
                    break

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *videos):
        self.videos = set(videos)

    def  get_videos(self, word_find):
        get_list_videos = list()
        for i in self.videos:
            if word_find.lower() in i.title.lower():
                get_list_videos.append(i.title)
        return get_list_videos

    def watch_video(self, name_video):

        if self.current_user:
            for video_watch in self.videos:
                if video_watch.title == name_video and video_watch.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
                elif (video_watch.title == name_video and video_watch.adult_mode and self.current_user.age > 18
                      or video_watch.title == name_video and video_watch.adult_mode == False):
                    for sec in range(1, video_watch.duration+1):
                        sleep(1)
                        video_watch.time_now = sec
                        print(video_watch.time_now, '', end='')
                    print('Конец')
                    video_watch.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

#         # Добавление видео
ur.add(v1, v2)
#         # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

#         # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

#          # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

#          # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')












