<template>
  <div>
    <h1>ddd</h1>
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
  async asyncData() {
    const services = await axios.get(`http://127.0.0.1:8000/api/tag/tag2`);
    return { services: services.data.results };
  }
}
</script>
