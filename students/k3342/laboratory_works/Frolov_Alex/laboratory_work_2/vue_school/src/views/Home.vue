<template>
    <mu-container>
        <mu-row>
            <mu-col>
<mu-carousel hide-controls>
  <mu-carousel-item>
    <img :src="carouselImg1">

</mu-carousel-item>
</mu-carousel>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
import carouselImg1 from 'C:/Users/Alex/Desktop/vue-images/img1.jpg';

    export default {
        name: 'Home',
        data () {
    return {
      carouselImg1,

    }
  }
    }
</script>
