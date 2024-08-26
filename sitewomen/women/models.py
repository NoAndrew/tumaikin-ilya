from django.db import models


class Women(models.Model):
    text = models.TextField(blank=True)
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    title4 = models.CharField(max_length=255)
    title5 = models.CharField(max_length=255)
    title6 = models.CharField(max_length=255, null=True, blank=True)
    content1 = models.CharField(max_length=255)
    content2 = models.CharField(max_length=255)
    content3 = models.CharField(max_length=255)
    content4 = models.CharField(max_length=255)
    content5 = models.CharField(max_length=255)
    content6 = models.CharField(max_length=255, null=True, blank=True)
    content7 = models.CharField(max_length=255, null=True, blank=True)
    content8 = models.CharField(max_length=255, null=True, blank=True)
    content9 = models.CharField(max_length=255, null=True, blank=True)
    content10 = models.CharField(max_length=255, null=True, blank=True)
    content11 = models.CharField(max_length=255, null=True, blank=True)
    content12 = models.CharField(max_length=255, null=True, blank=True)
    content13 = models.CharField(max_length=255, null=True, blank=True)
    content14 = models.CharField(max_length=255, null=True, blank=True)
    content15 = models.CharField(max_length=255, null=True, blank=True)
    content16 = models.CharField(max_length=255, null=True, blank=True)
    content17 = models.CharField(max_length=255, null=True, blank=True)
    content18 = models.CharField(max_length=255, null=True, blank=True)
    content19 = models.CharField(max_length=255, null=True, blank=True)
    content20 = models.CharField(max_length=255, null=True, blank=True)
    content21 = models.CharField(max_length=255, null=True, blank=True)
    content22 = models.CharField(max_length=255, null=True, blank=True)
    content23 = models.CharField(max_length=255, null=True, blank=True)
    content24 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Материалы'
        verbose_name_plural = 'Страница сайта "Материалы"'


class Women2(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    title4 = models.CharField(max_length=255)
    title5 = models.CharField(max_length=255)
    title6 = models.CharField(max_length=255)
    content1 = models.CharField(max_length=255)
    content2 = models.CharField(max_length=255)
    content3 = models.CharField(max_length=255)
    content4 = models.CharField(max_length=255)
    content5 = models.CharField(max_length=255)
    content6 = models.CharField(max_length=255)
    content7 = models.CharField(max_length=255)
    content8 = models.CharField(max_length=255)
    content9 = models.CharField(max_length=255)

    ad_title = models.CharField(max_length=255, null=True, blank=True)
    ad_title_down = models.CharField(max_length=255, null=True, blank=True)
    white_title = models.CharField(max_length=255, null=True, blank=True)
    white_ad_title = models.CharField(max_length=255, null=True, blank=True)
    blue_title = models.CharField(max_length=255, null=True, blank=True)
    title_blue1 = models.CharField(max_length=255, null=True, blank=True)
    content_blue1 = models.CharField(max_length=255, null=True, blank=True)
    title_blue2 = models.CharField(max_length=255, null=True, blank=True)
    content_blue2 = models.CharField(max_length=255, null=True, blank=True)
    title_blue3 = models.CharField(max_length=255, null=True, blank=True)
    content_blue3 = models.CharField(max_length=255, null=True, blank=True)
    content_blue4 = models.CharField(max_length=255, null=True, blank=True)
    title_blue4 = models.CharField(max_length=255, null=True, blank=True)
    content_blue5 = models.CharField(max_length=255, null=True, blank=True)
    title_blue5 = models.CharField(max_length=255, null=True, blank=True)
    content_blue6 = models.CharField(max_length=255, null=True, blank=True)
    title_blue6 = models.CharField(max_length=255, null=True, blank=True)
    content_blue7 = models.CharField(max_length=255, null=True, blank=True)
    content_blue8 = models.CharField(max_length=255, null=True, blank=True)

    green_title = models.CharField(max_length=255, null=True, blank=True)
    green_ad_title = models.CharField(max_length=255, null=True, blank=True)
    title_green = models.CharField(max_length=255, null=True, blank=True)
    title_green1 = models.CharField(max_length=255, null=True, blank=True)
    content_green1 = models.CharField(max_length=255, null=True, blank=True)
    title_green2 = models.CharField(max_length=255, null=True, blank=True)
    content_green2 = models.CharField(max_length=255, null=True, blank=True)
    title_green3 = models.CharField(max_length=255, null=True, blank=True)
    content_green3 = models.CharField(max_length=255, null=True, blank=True)
    content_green4 = models.CharField(max_length=255, null=True, blank=True)
    title_green4 = models.CharField(max_length=255, null=True, blank=True)
    content_green5 = models.CharField(max_length=255, null=True, blank=True)
    title_green5 = models.CharField(max_length=255, null=True, blank=True)
    content_green6 = models.CharField(max_length=255, null=True, blank=True)
    title_green6 = models.CharField(max_length=255, null=True, blank=True)
    content_green7 = models.CharField(max_length=255, null=True, blank=True)
    content_green8 = models.CharField(max_length=255, null=True, blank=True)

    yellow_title = models.CharField(max_length=255, null=True, blank=True)
    yellow_ad_title = models.CharField(max_length=255, null=True, blank=True)
    title_yellow = models.CharField(max_length=255, null=True, blank=True)
    title_yellow1 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow1 = models.CharField(max_length=255, null=True, blank=True)
    title_yellow2 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow2 = models.CharField(max_length=255, null=True, blank=True)
    title_yellow3 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow3 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow4 = models.CharField(max_length=255, null=True, blank=True)
    title_yellow4 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow5 = models.CharField(max_length=255, null=True, blank=True)
    title_yellow5 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow6 = models.CharField(max_length=255, null=True, blank=True)
    title_yellow6 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow7 = models.CharField(max_length=255, null=True, blank=True)
    content_yellow8 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Страница сайта "Обо мне"'


class Women5(models.Model):
    title1 = models.CharField(max_length=255)
    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    title2 = models.CharField(max_length=255)
    card1 = models.CharField(max_length=255)
    card2 = models.CharField(max_length=255)
    card3 = models.CharField(max_length=255)
    text_card1 = models.TextField(blank=True)
    text_card2 = models.TextField(blank=True)
    text_card3 = models.TextField(blank=True)
    content1 = models.CharField(max_length=255)
    content2 = models.CharField(max_length=255)
    content3 = models.CharField(max_length=255)
    content4 = models.CharField(max_length=255)
    content5 = models.CharField(max_length=255)
    content6 = models.TextField(blank=True)
    content7 = models.TextField(blank=True)
    content8 = models.TextField(blank=True)
    content9 = models.CharField(max_length=255)
    content10 = models.TextField(blank=True)
    content11 = models.TextField(blank=True)
    content12 = models.TextField(blank=True)
    content13 = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Достижение учеников'
        verbose_name_plural = 'Страница сайта "Достижение учеников"'


class Women6(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    title4 = models.CharField(max_length=255)
    title5 = models.CharField(max_length=255)
    title6 = models.CharField(max_length=255)
    title7 = models.CharField(max_length=255)
    title8 = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_blue = models.CharField(max_length=255)
    title_blue_down = models.CharField(max_length=255)
    title_white = models.CharField(max_length=255)
    title_white_down = models.CharField(max_length=255)
    title_blue_in = models.CharField(max_length=255)
    title_blue_in_down1 = models.CharField(max_length=255)
    title_blue_in_down2 = models.CharField(max_length=255)
    title_blue_in_down3 = models.CharField(max_length=255)
    title_blue_in_down4 = models.CharField(max_length=255)
    title_blue_in_down5 = models.CharField(max_length=255)
    text_blue1 = models.TextField(blank=True)
    text_blue2 = models.TextField(blank=True)
    text_blue3 = models.TextField(blank=True)
    text_blue4 = models.TextField(blank=True)
    text_blue5 = models.TextField(blank=True)
    text_blue6 = models.TextField(blank=True)
    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    text4 = models.TextField(blank=True)
    text5 = models.TextField(blank=True)
    text6 = models.TextField(blank=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)
    content6 = models.TextField(blank=True)
    content7 = models.TextField(blank=True)
    content8 = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Олимпиады'
        verbose_name_plural = 'Страница сайта "Олимпиады"'


class Women4(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    content1 = models.CharField(max_length=255)
    content2 = models.CharField(max_length=255)
    content3 = models.CharField(max_length=255)
    name_pages = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Страница сайта "Главная"'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name




