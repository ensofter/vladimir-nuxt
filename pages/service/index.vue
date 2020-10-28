<template>
  <div>
    <h1>Все записи блога</h1>
    <div class="blog-links-block">
      <nuxt-link to="/service/tag1">статьи о моче</nuxt-link>
      <nuxt-link to="/service/tag2">статьи о говне</nuxt-link>
      <nuxt-link to="/service/tag3">статьи о жопе</nuxt-link>
      <nuxt-link to="/service/tag4">статьи о гомиках</nuxt-link>
      <nuxt-link to="/service" prefetch="false">услуги</nuxt-link>
    </div>
    <div class="blog-block">
      <div v-for="service in services" :key="service.id" class="blog">
        <nuxt-link :to="`/service/${service.slug}`">
          <img :src="service.image">
          <div class="blog-title">{{ service.h1 }}</div>
          <div class="blog-introtext">{{ service.intro }}</div>
          <div class="blog-tag">{{ service.tag }}</div>
        </nuxt-link>

      </div>
    </div>
    <div class="blog-pagination-block">
      <nuxt-link :to="`/service${previous}`" v-if="previous != null">Назад</nuxt-link>
      <nuxt-link :to="`/service${next}`" v-if="next != null">Вперед</nuxt-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      services: [],
      next: [],
      previous: [],
    }
  },
  watchQuery: ['page'],
  async asyncData({route}) {
    let page = route.query.page !== undefined ? `?page=${route.query.page}` : '';
    const { data } = await axios.get(`http://127.0.0.1:8000/api/services/${page}`);
    let next = data.next != null ? data.next.split('/')[5] : data.next;
    let previous = data.previous != null ? data.previous.split('/')[5] : data.previous;
    return {
      services: data.results,
      total: data.count / 4,
      next: next,
      previous: previous,
    };
  },
  head() {
    return {
      title: "Услуги",
      meta: [
        { hid: "description", name: "description", content: "Это страница услуг"}
      ]
    };
  },
}
</script>
