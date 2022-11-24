<template>
  
  <carousel-3d :autoplay="false" :autoplayHoverPause="true" :perspective="10" :space="300">
        <slide v-for="(slide, i) in slides" :index="i" :key="i">
          <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
            <div 
              :data-index="index" 
              :class="{ 
                current: isCurrent, 
                onLeft: (leftIndex >= 0), 
                onRight: (rightIndex >= 0) 
                }" 
              :src="posterImg + slide.poster_path "
              style="z-index: -1; positon: relative;"
            >
            </div>
          </template>
        </slide>
  </carousel-3d>

</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: "MovieCarousel",
  data() {
      return {

      }
    },
  components: {
    Carousel3d,
    Slide
  },
  computed: {
    slides() {
        return this.$store.state.movies
      },
    posterImg() {
    const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/'
    return imgurl
    }
  },
}
</script>

<style>

</style>