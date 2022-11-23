<template>
  <div>
    <h1>Wish List</h1>
    <WishListDetail v-if="tooDetail" :toWishDetail="toWishDetail" />
    <WishListItems
      class="wishlist-items"
      v-for="wishlist in wishlists"
      :key="wishlist.id"
      :wishlist="wishlist"
      :user_id="user_id"
      @renew-my-wishlists="wishListMovie"
      @wishmovie-detail="wishMovieDetail"
    />
  </div>
</template>

<script>
import WishListItems from "@/components/WishListItems";
import WishListDetail from "@/components/WishListDetail";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "WishList",
  components: {
    WishListItems,
    WishListDetail,
  },
  data() {
    return {
      wishlists: [],
      user_id: null,
      username: null,
      toWishDetail: [],
      tooDetail: false,
    };
  },

  computed: {
    wishMovie() {
      return this.wishlists;
    },
  },
  created() {
    this.getUserPk();
  },
  methods: {
    getUserPk() {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.user_id = res.data.pk;
        this.username = res.data.username;
        this.wishListMovie();
        return { user_id: res.data.pk };
      });
    },
    wishListMovie() {
      axios({
        method: "get",
        url: `${API_URL}/movies/wish_list/${this.user_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log("dddd", res.data);
          this.$store.dispatch("saveWishList", res.data);
          return res.data;
        })
        .then((last) => {
          this.wishlists = this.$store.state.wishlist;
          return last;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    wishMovieDetail(movie_data) {
      this.toWishDetail = movie_data;
      this.tooDetail = true;
      console.log("가보자고", this.toWishDetail);
    },
  },
};
</script>

<style>
</style>