<template>
  <div>
    <Header/>
    <div class="content center">
      <Nuxt/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from "~/components/Header";
import Footer from "@/components/Footer";
export default {
  head() {
    return {
      link: [
        { rel: "canonical", href: `http://localhost:3000${this.$route.path}`}
      ]
    }
  },
  components: {
    Header,
    Footer
  }
}
</script>
