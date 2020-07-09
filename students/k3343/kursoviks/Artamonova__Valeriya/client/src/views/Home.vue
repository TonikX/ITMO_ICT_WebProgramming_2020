<template>
    <mu-container>
        <mu-row>
            <mu-col>
<mu-carousel hide-controls>
  <mu-carousel-item>
    <img :src="carouselImg1">
  </mu-carousel-item>
  <mu-carousel-item>
    <img :src="carouselImg2">
  </mu-carousel-item>
  <mu-carousel-item>
    <img :src="carouselImg3">
  </mu-carousel-item>
  <mu-carousel-item>
    <img :src="carouselImg4">
  </mu-carousel-item>
</mu-carousel>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
import carouselImg1 from 'C:/Users/User/Desktop/Учеба/3 курс 6 семестр/Web-программирование/pic/pic1.jpg';
import carouselImg2 from 'C:/Users/User/Desktop/Учеба/3 курс 6 семестр/Web-программирование/pic/pic2.jpg';
import carouselImg3 from 'C:/Users/User/Desktop/Учеба/3 курс 6 семестр/Web-программирование/pic/pic3.jpg';
import carouselImg4 from 'C:/Users/User/Desktop/Учеба/3 курс 6 семестр/Web-программирование/pic/pic4.jpg';

    export default {
        name: 'Home',
        data () {
    return {
      carouselImg1,
      carouselImg2,
      carouselImg3,
      carouselImg4
    }
  }
    }
</script>
