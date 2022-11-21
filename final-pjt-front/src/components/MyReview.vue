<template>
  <div>
    <h1>My Reviews</h1>
    <MyReviewItems/>
  </div>
</template>

<script>
import MyReviewItems from '@/components/MyReviewItems'
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name : "MyReviews",
  components: {
    MyReviewItems,
  },
  data() {
    return {
      reviews : null,
    }
  },
  // created() {
  //   axios({
  //       method: 'post',
  //       url: `${API_URL}/movies/my_review/<int:user_pk>/`,
  //       data: {
  //         movie_pk: payload.username,
  //         user_pk: payload.password,
  //       }
  //     })
  //       .then((res) => {
  //         console.log(res)
  //       })
  // }
}
</script>

<style>

</style>