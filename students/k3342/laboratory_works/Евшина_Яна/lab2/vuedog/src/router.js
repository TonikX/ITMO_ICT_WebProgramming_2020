import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  linkActiveClass: "active",
  routes: [
    {
      path: "/login",
      name: "sign-in",
      component: () => import("./views/LoginPage.vue"),
    },
    {
      path: "/register",
      name: "sign-up",
      component: () => import("./views/RegistrationPage.vue"),
    },
    {
      path: "/",
      component: () => import("./views/IndexPage.vue"),
      children: [
        {
          path: "/",
          name: "home",
          component: () => import("./views/HomePage.vue"),
        },
        {
          path: "/dogs",
          name: "dogs",
          component: () => import("./views/DogsPage.vue"),
        },
        {
          path: "/clubs",
          name: "clubs",
          component: () => import("./views/ClubsPage.vue"),
        },
        {
          path: '/shows/:id',
          name: "show",
          component: () => import("./views/ShowPage.vue"),
        },
        // {
        //   path: "/courses/:courseId",
        //   name: "course-detail",
        //   component: () => import("./views/CourseDetailBasePage.vue"),
        //   beforeEnter: (to, from, next) => {
        //     ifParamIsNumber(to.params.courseId, "/courses", next);
        //   },
        //   props: (route) => {
        //     const courseId = Number.parseInt(route.params.courseId, 10);
        //     return { courseId };
        //   }
        // },
        // {
        //   path: "/courses/:courseId/submissions/:submissionId",
        //   name: "submission-detail",
        //   component: () => import("./views/SubmissionDetailedPage.vue"),
        //   beforeEnter: (to, from, next) => {
        //     ifParamIsNumber(to.params.courseId, "/courses", next);
        //     ifParamIsNumber(to.params.submissionId, "/courses", next);
        //   },
        //   props: (route) => {
        //     const courseId = Number.parseInt(route.params.courseId, 10);
        //     const submissionId = Number.parseInt(route.params.submissionId, 10);
        //     return { courseId, submissionId };
        //   },
        // },
        // {
        //   path: "submissions",
        //   name: "submissions",
        //   component: () => import("./views/SubmissionsPage.vue")
        // },
        // {
        //   path: "create-course",
        //   name: "create-course",
        //   component: () => import("./views/CourseCreationPage.vue")
        // }
      ]
    },
    // {
    //   path: "/register",
    //   name: "sign-up",
    //   component: () => import("./views/RegisterPage.vue")
    // },
    // {
    //   path: "*",
    //   component: () => import("./views/NotFoundPage.vue")
    // }
  ]
});

router.beforeEach((to, from, next) => {
  const publicPages = ["/login", "/register"];
  const authRequired = !publicPages.includes(to.path);
  const tokens = JSON.parse(localStorage.getItem("tokens"));

  if (authRequired && !tokens) {
    return next("/login");
  }

  if (!authRequired && tokens) {
    return next("/");
  }

  next();
});

export default router;