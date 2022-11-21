<template>
  <div>
    <h1>My Reviews</h1>
    <MyReviewItems
    class="review-items"
    v-for="review in reviews"
    :key="review.id"
    :review="review"
    />
  </div>
</template>

<script>
import MyReviewItems from '@/components/MyReviewItems'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : "MyReviews",
  components: {
    MyReviewItems,
  },
  data() {
    return {
      reviews : null,
      user_id : null,
      username: null,
    }
  },
  created() {
    this.getUserPk()
  },
  methods: {
    getUserPk() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.user_id = res.data.pk
          this.username = res.data.username
          return {'user_id': res.data.pk}
        })
        .then((res) => {
          const user_id = res.user_id
          axios({
            method: 'get',
            url: `${API_URL}/movies/my_review/${user_id}/`,
            data: {
              user_pk: user_id,
            },
            headers: {
              Authorization: `Token ${ this.$store.state.token }`
            }
          })
            .then((res) => {
              this.reviews = res.data
              console.log(res.data)
            })
        })
    }
  }
}
</script>

<style>

</style>