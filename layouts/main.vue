<template>
  <div>
    <Header/>
    <Nuxt />
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
        { rel: "canonical", href: "http://localhost:3000"}
      ]
    }
  },
  components: {
    Header,
    Footer
  }
}
</script>
