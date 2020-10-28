<template>
  <div>
    <h1>{{ service.h1 }}</h1>
    <ul class="breadcrumbs" itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <nuxt-link to="/" itemid="/" itemtype="https://schema.org/Thing" itemscope itemprop="item">
          <span itemprop="name">Главная</span>
        </nuxt-link><span class="breadcrumbs-arrow">&gt;</span>
        <meta itemprop="position" content="1">
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <nuxt-link to="/service" itemid="/service/" itemtype="https://schema.org/Thing" itemscope itemprop="item">
          <span itemprop="name">Услуги</span>
        </nuxt-link><span class="breadcrumbs-arrow">&gt;</span>
        <meta itemprop="position" content="2">
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span itemprop="name">{{ service.h1 }}</span>
        <meta itemprop="position" content="3">
      </li>
    </ul>

    <div class="blog-plus-aside">
      <div class="content">
        <div v-html="service.content"></div>
        <div class="blog-author-blog">
          <strong>Автор:</strong>
          <span>Алексей Ромашов</span>.
          <strong>Опубликовано:</strong> {{ $dateFns.format(service.created, 'dd.MM.yyyy') }}
        </div>
        <div class="yandex-share-block">
        <strong>Поделиться</strong>
          <div class="ya-share2" data-services="vkontakte,facebook,odnoklassniki,twitter,viber,whatsapp,telegram"></div>
        </div>
      </div>

      <aside>
        <a href="//" rel="noreferrer nofollow" target="_blank" class="youtube-button">
          <span>Продвижение сайтов в прямом эфире</span>
        </a>
        <div class="aside-blog-block">
          <div v-for="item in aside" :key="item._id" class="blog">
            <nuxt-link :to="`/service/${item.slug}`">
              <img :src="item.image">
              <div class="blog-title">{{ item.h1 }}</div>
            </nuxt-link>
          </div>
        </div>
      </aside>

    </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  async asyncData({ params }) {
    const service  = await axios.get(`http://127.0.0.1:8000/api/services/${params.slug}`);
    const aside  = await axios.get(`http://127.0.0.1:8000/api/aside`);
    return {
      service: service.data,
      aside: aside.data
    }
  },
  head() {
    return {
      script: [
        {src: '//yastatic.net/es5-shims/0.0.2/es5-shims.min.js', body: true, async: true},
        {src: '//yastatic.net/share2/share.js', body: true, async: true}
      ],
      title: this.service.title,
      meta: [
        {
          hid: "description",
          name: "description",
          content: "Это страница услуг"
        },
        {
          property: "og:url",
          content: `http://pupa.ru${this.$route.path}`
        },
        {
          property: "og:type",
          content: "website"
        },
        {
          property: "og:title",
          content: `${this.service.title}`
        },
        {
          property: "og:description",
          content: `${this.service.intro}`
        },
        {
          property: "og:site_name", content: "Pupa.ru"
        },
        {
          property: "og:locale", content: "ru_RU"
        },
        {
          property: "og:image",
          content: "http://dfghjk"
        },
        {
          property: "og:image:alt",
          content: "ОПАНА"
        },
        {
          property: "fb:app_id", content: "23456789"
        },
        {
          name: "twitter:card", content: "summary_large_image"
        },
        {
          name: "twitter:site", content: "@opa"
        },
        {
          name: "twitter.title",
          content: `${this.service.title}`
        },
        {
          name: "twitter:description",
          content: `${this.service.intro}`
        },
        {
          name: "twitter:image:src",
          content: "http://dfsdf.com"
        }
      ]
    };
  },

}
</script>

<style scoped>

</style>
