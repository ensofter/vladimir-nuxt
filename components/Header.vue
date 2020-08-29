<template>
  <header>
    <div class="center">
      <nav>
        <nuxt-link to="/">Главная</nuxt-link>
        <nuxt-link to="/uslugi">Услуги</nuxt-link>
        <nuxt-link to="/keisi">Кейсы</nuxt-link>
        <nuxt-link to="/blog">Блог</nuxt-link>
        <nuxt-link to="/kontakti">Контакты</nuxt-link>
        <nuxt-link to="/wiki">SEO</nuxt-link>
      </nav>

      <div class="header-contacts">
        <div class="header-contacts-name">Алексей Ромашов</div>
        <div class="header-contacts-phone">
          <a href="tel:89522077765">+7 952 207-77-65</a>
          <a href="mailto:amromashov@gmail.com" target="_blank"> amromashov@gmail.com</a>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>

</style>
