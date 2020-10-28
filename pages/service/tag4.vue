<template>
  <div>
    <h1>DFFF</h1>
    <div class="blog-links-block">
      <nuxt-link to="/service/tag1">статьи о моче</nuxt-link>
      <nuxt-link to="/service/tag2">статьи о говне</nuxt-link>
      <nuxt-link to="/service/tag3">статьи о жопе</nuxt-link>
      <nuxt-link to="/service/tag4">статьи о гомиках</nuxt-link>
    </div>
    <div class="blog-block">
      <div v-for="service in services" :key="service.id" class="blog">
        <nuxt-link :to="`/service/${service.slug}`">
          <img :src="service.image">
          <div class="blog-title">{{ service.h1 }}</div>
          <div class="blog-introtext">{{ service.intro }}</div>
          <div class="blog-tag">{{ $dateFns.format(service.created, 'dd.MM.yyyy') }}</div>
        </nuxt-link>
      </div>
    </div>
    <div class="blog-pagination-block">
      <nuxt-link :to="`/service/tag4${previous}`" v-if="previous != null">Назад</nuxt-link>
      <nuxt-link :to="`/service/tag4${next}`" v-if="next != null">Вперед</nuxt-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  head() {
    return {
      title: "Услуги",
      meta: [
        { hid: "description", name: "description", content: "Это страница услуг"}
      ]
    };
  },
  watchQuery: ['page'],
  async asyncData({route}) {
    let page = route.query.page !== undefined ? `?page=${route.query.page}` : '';
    const services = await axios.get(`http://127.0.0.1:8000/api/tag/tag4/${page}`);
    let next = services.data.next != null ? services.data.next.split('/')[6] : services.data.next;
    let previous = services.data.previous != null ? services.data.previous.split('/')[6] : services.data.previous;
    console.log(next)
    return {
      services: services.data.results,
      total: services.data.count / 4,
      next: next,
      previous: previous,
    };
  }
}
</script>
