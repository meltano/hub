<template>
  <div class="w-full max-w-4xl px-3 mx-auto">
    <div class="text-center">
      <h2 class="mb-4 text-3xl font-bold text-black md:text-4xl lg:text-5xl">
        Connectors for <span class="brackets brackets-blue">everything</span>
      </h2>
      <p class="font-normal opacity-75 text-black/75 text-md font-grotesk">
        Extract an load data from any application, database, and file
      </p>
    </div>

    <div class="grid grid-cols-6 gap-2 my-10 md:grid-cols-8 lg:grid-cols-12">
      <div v-for="(item, index) in logos" :key="index + 'item'">
        <!-- TODO: Add URLs -->
        <a
          href="#"
          class="flex items-center justify-center bg-white rounded-sm hover:shadow-lg aspect-square"
        >
          <img class="block w-16 h-16 mx-auto" :src="item" alt="Item name" />
        </a>
      </div>
    </div>

    <div class="flex flex-wrap justify-center -mx-1.5">
      <div class="px-1.5 py-2" v-for="(item, idx) in btns" :key="item.name + '-' + idx">
        <a
          :href="item.url"
          class="bg-blue text-[15px] flex flex-row justify-center font-ibm text-white items-center w-auto rounded-md px-4 py-2.5 border border-blue leading-tight hover:bg-purple hover:border-purple"
        >
          <component class="bg-white/20 rounded-full text-white mr-2.5" :is="item.icon" />
          {{ item.name }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import IconPlus from "../icons/IconPlus.vue";
import IconMagnifier from "../icons/IconMagnifier.vue";
import IconGear from "../icons/IconGear.vue";

import logo63 from "../../assets/images/connectors/logo-63.svg";
import logo1 from "../../assets/images/connectors/logo-1.svg";
import logo2 from "../../assets/images/connectors/logo-2.svg";
import logo3 from "../../assets/images/connectors/logo-3.svg";
import logo4 from "../../assets/images/connectors/logo-4.svg";
import logo5 from "../../assets/images/connectors/logo-5.svg";
import logo6 from "../../assets/images/connectors/logo-6.svg";
import logo7 from "../../assets/images/connectors/logo-7.svg";
import logo8 from "../../assets/images/connectors/logo-8.svg";
import logo9 from "../../assets/images/connectors/logo-9.svg";
import logo10 from "../../assets/images/connectors/logo-10.svg";
import logo11 from "../../assets/images/connectors/logo-11.svg";
import logo12 from "../../assets/images/connectors/logo-12.svg";
import logo13 from "../../assets/images/connectors/logo-13.svg";
import logo14 from "../../assets/images/connectors/logo-14.svg";
import logo15 from "../../assets/images/connectors/logo-15.svg";
import logo16 from "../../assets/images/connectors/logo-16.svg";
import logo17 from "../../assets/images/connectors/logo-17.svg";
import logo18 from "../../assets/images/connectors/logo-18.svg";
import logo19 from "../../assets/images/connectors/logo-19.svg";
import logo20 from "../../assets/images/connectors/logo-20.svg";
import logo21 from "../../assets/images/connectors/logo-21.svg";
import logo22 from "../../assets/images/connectors/logo-22.svg";
import logo23 from "../../assets/images/connectors/logo-23.svg";
import logo24 from "../../assets/images/connectors/logo-24.svg";
import logo25 from "../../assets/images/connectors/logo-25.svg";
import logo26 from "../../assets/images/connectors/logo-26.svg";
import logo27 from "../../assets/images/connectors/logo-27.svg";
import logo28 from "../../assets/images/connectors/logo-28.svg";
import logo29 from "../../assets/images/connectors/logo-29.svg";
import logo30 from "../../assets/images/connectors/logo-30.svg";
import logo31 from "../../assets/images/connectors/logo-31.svg";
import logo32 from "../../assets/images/connectors/logo-32.svg";
import logo33 from "../../assets/images/connectors/logo-33.svg";
import logo34 from "../../assets/images/connectors/logo-34.svg";
import logo35 from "../../assets/images/connectors/logo-35.svg";
import logo36 from "../../assets/images/connectors/logo-36.svg";
import logo37 from "../../assets/images/connectors/logo-37.svg";
import logo38 from "../../assets/images/connectors/logo-38.svg";
import logo39 from "../../assets/images/connectors/logo-39.svg";
import logo40 from "../../assets/images/connectors/logo-40.svg";
import logo41 from "../../assets/images/connectors/logo-41.svg";
import logo42 from "../../assets/images/connectors/logo-42.svg";
import logo43 from "../../assets/images/connectors/logo-43.svg";
import logo44 from "../../assets/images/connectors/logo-44.svg";
import logo45 from "../../assets/images/connectors/logo-45.svg";
import logo46 from "../../assets/images/connectors/logo-46.svg";
import logo47 from "../../assets/images/connectors/logo-47.svg";
import logo48 from "../../assets/images/connectors/logo-48.svg";
import logo49 from "../../assets/images/connectors/logo-49.svg";
import logo50 from "../../assets/images/connectors/logo-50.svg";
import logo51 from "../../assets/images/connectors/logo-51.svg";
import logo52 from "../../assets/images/connectors/logo-52.svg";
import logo53 from "../../assets/images/connectors/logo-53.svg";
import logo54 from "../../assets/images/connectors/logo-54.svg";
import logo55 from "../../assets/images/connectors/logo-55.svg";
import logo56 from "../../assets/images/connectors/logo-56.svg";
import logo57 from "../../assets/images/connectors/logo-57.svg";
import logo58 from "../../assets/images/connectors/logo-58.svg";
import logo59 from "../../assets/images/connectors/logo-59.svg";
import logo60 from "../../assets/images/connectors/logo-60.svg";
import logo61 from "../../assets/images/connectors/logo-61.svg";
import logo62 from "../../assets/images/connectors/logo-62.svg";
import logo64 from "../../assets/images/connectors/logo-64.svg";
import logo65 from "../../assets/images/connectors/logo-65.svg";
import logo66 from "../../assets/images/connectors/logo-66.svg";
import logo67 from "../../assets/images/connectors/logo-67.svg";
import logo68 from "../../assets/images/connectors/logo-68.svg";
import logo69 from "../../assets/images/connectors/logo-69.svg";
import logo70 from "../../assets/images/connectors/logo-70.svg";
import logo71 from "../../assets/images/connectors/logo-71.svg";
import logo72 from "../../assets/images/connectors/logo-72.svg";

/* Add URLs */
const btns = [
  { name: "Explore Connectors", url: "#", icon: IconMagnifier },
  { name: "Build a Connector", url: "#", icon: IconGear },
  { name: "Publish a Connector", url: "#", icon: IconPlus },
];

const logos = [
  logo63,
  logo1,
  logo2,
  logo3,
  logo4,
  logo5,
  logo6,
  logo7,
  logo8,
  logo9,
  logo10,
  logo11,
  logo12,
  logo13,
  logo14,
  logo15,
  logo16,
  logo17,
  logo18,
  logo19,
  logo20,
  logo21,
  logo22,
  logo23,
  logo24,
  logo25,
  logo26,
  logo27,
  logo28,
  logo29,
  logo30,
  logo31,
  logo32,
  logo33,
  logo34,
  logo35,
  logo36,
  logo37,
  logo38,
  logo39,
  logo40,
  logo41,
  logo42,
  logo43,
  logo44,
  logo45,
  logo46,
  logo47,
  logo48,
  logo49,
  logo50,
  logo51,
  logo52,
  logo53,
  logo54,
  logo55,
  logo56,
  logo57,
  logo58,
  logo59,
  logo60,
  logo61,
  logo62,
  logo64,
  logo65,
  logo66,
  logo67,
  logo68,
  logo69,
  logo70,
  logo71,
  logo72,
];

export default {
  components: {
    IconPlus,
    IconMagnifier,
    IconGear,
  },
  name: "HeroConnectors",
  data() {
    return {
      btns,
      logos,
    };
  },
};
</script>
