<template>
  <div class="app">
    <p>{{ name }}</p>
    <button @click="changeName('adfsdf')">change name</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';


export default defineComponent({
  name: 'App',
  components: {
    
  },
  data() {
    return {
      name: 'link'
    }
  },
  methods: {
    changeName(name: string) {
      this.name = name
    }
  }
});
</script>

<style>

</style>
