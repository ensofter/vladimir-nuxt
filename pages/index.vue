<template>
  <div class="content">
    <div class="main-gradient-block">
      <h1>Эффективный и понятный интернет маркетинг</h1>
    </div>
    <div class="main-plus-block center">
      <div class="main-plus">
        <div class="main-plus-ico main-plus-ico-1"></div>
        <div class="main-plus-text">
          Работаю на результат<br>
          а не ради отчетов
        </div>
      </div>
      <div class="main-plus">
        <div class="main-plus-ico main-plus-ico-2"></div>
        <div class="main-plus-text">
          Работаю на результат<br>
          а не ради отчетов
        </div>
      </div>
      <div class="main-plus">
        <div class="main-plus-ico main-plus-ico-3"></div>
        <div class="main-plus-text">
          Работаю на результат<br>
          а не ради отчетов
        </div>
      </div>
      <div class="main-plus">
        <div class="main-plus-ico main-plus-ico-4"></div>
        <div class="main-plus-text">
          Работаю на результат<br>
          а не ради отчетов
        </div>
      </div>
    </div>
    <div class="main-utp-text">
      Интеграл от функции, обращающейся в бесконечность вдоль линии порождает винил.
      <br> Внутридискретное арпеджио использует действительный интеграл Фурье.
      <br> Развивая эту тему, техника сонорна.
    </div>
    <h2>Компании</h2>
    <div class="clients-block center">
      <img alt="Правовая защита"  src="/img/logo-13.jpg">
      <img alt="Диспетчерская 33" src="/img/logo-1.jpg">
      <img alt="Кен" src="/img/logo-2.jpg">
      <img alt="ШильдПанель" src="/img/logo-4.jpg">
      <img alt="Лаборатория труда" src="/img/logo-6.jpg">
      <img alt="Фитнес-тренер Дарья Жичкина" src="/img/logo-5.jpg">
      <img alt="Техсоюз Плюс" src="/img/logo-7.jpg">
      <img alt="МаксС" src="/img/logo-8.jpg">
      <img alt="Вторма" src="/img/logo-11.jpg">
      <img alt="Кар 33" src="/img/logo-16.jpg">
      <img alt="Оранжевый уровень" src="/img/logo-12.jpg">
      <img alt="Спецтехперевозки" src="/img/logo-3.jpg">
      <img alt="Бизнес омбудсмен" src="/img/logo-14.jpg">
      <img alt="ЛДПР" src="/img/logo-9.jpg">
      <img alt="Опора России" src="/img/logo-10.jpg">
      <img alt="Вендинговая компания" src="/img/logo-15.jpg">
    </div>
    <h2>Свежие записи блога</h2>
    <div class="main-blogs-block center">
      <div v-for="blog in blogs" :key="blog.id" class="blog">
        <nuxt-link :to="`/service/${blog.slug}`">
          <img :src="blog.image">
          <div class="blog-title">{{ blog.h1 }}</div>
          <div class="blog-introtext">{{ blog.intro }}</div>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  layout: 'main',
  async asyncData({ params }) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/aside`);
    return {
      blogs: data
    }
  },
  head() {
    return {
      title: "Главная страница",
      meta: [
        { hid: "description", name: "description", content: "Это главная"}
      ]
    }
  },
  data() {
    return {
      swiperOptions: {
        pagination: {
          el: '.swiper-pagination'
        },
        // Some Swiper option/callback...
      }
    }
  },
}
</script>

<style>
</style>
