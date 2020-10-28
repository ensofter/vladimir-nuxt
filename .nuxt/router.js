import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _35b3531f = () => interopDefault(import('../pages/service/index.vue' /* webpackChunkName: "pages/service/index" */))
const _4f66a5e5 = () => interopDefault(import('../pages/service/blog.vue' /* webpackChunkName: "pages/service/blog" */))
const _46b7879a = () => interopDefault(import('../pages/service/tag1.vue' /* webpackChunkName: "pages/service/tag1" */))
const _46c59f1b = () => interopDefault(import('../pages/service/tag2.vue' /* webpackChunkName: "pages/service/tag2" */))
const _46d3b69c = () => interopDefault(import('../pages/service/tag3.vue' /* webpackChunkName: "pages/service/tag3" */))
const _46e1ce1d = () => interopDefault(import('../pages/service/tag4.vue' /* webpackChunkName: "pages/service/tag4" */))
const _33fcb1d7 = () => interopDefault(import('../pages/service/_slug.vue' /* webpackChunkName: "pages/service/_slug" */))
const _db2e360e = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/service",
    component: _35b3531f,
    name: "service"
  }, {
    path: "/service/blog",
    component: _4f66a5e5,
    name: "service-blog"
  }, {
    path: "/service/tag1",
    component: _46b7879a,
    name: "service-tag1"
  }, {
    path: "/service/tag2",
    component: _46c59f1b,
    name: "service-tag2"
  }, {
    path: "/service/tag3",
    component: _46d3b69c,
    name: "service-tag3"
  }, {
    path: "/service/tag4",
    component: _46e1ce1d,
    name: "service-tag4"
  }, {
    path: "/service/:slug",
    component: _33fcb1d7,
    name: "service-slug"
  }, {
    path: "/",
    component: _db2e360e,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
