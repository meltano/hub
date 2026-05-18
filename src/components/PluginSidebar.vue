<template>
  <div class="px-2 w-full lg:w-4/12">
    <div>
      <div class="community-card">
        <!-- Meltano Community section -->
        <div class="community-card__section">
          <div class="community-card__title-row">
            <svg
              class="community-card__section-icon"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
            >
              <g transform="translate(0.21, 4.5)">
                <path
                  d="M15.2099 13.8426C15.2837 13.9558 15.3256 14.0867 15.3311 14.2217C15.3366 14.3567 15.3055 14.4907 15.2412 14.6095C15.1768 14.7283 15.0816 14.8275 14.9655 14.8966C14.8495 14.9658 14.7169 15.0023 14.5818 15.0023H0.749908C0.614811 15.0023 0.482226 14.9658 0.366162 14.8966C0.250097 14.8275 0.154863 14.7283 0.0905218 14.6095C0.0261802 14.4907 -0.00488012 14.3567 0.000622504 14.2217C0.00612513 14.0867 0.0479864 13.9558 0.121783 13.8426C1.17751 12.2176 2.73037 10.9774 4.54866 10.3073C3.54347 9.63809 2.78032 8.66317 2.37206 7.52671C1.96381 6.39024 1.93212 5.15256 2.28168 3.99669C2.63125 2.84082 3.3435 1.82813 4.31313 1.10837C5.28276 0.388613 6.45827 0 7.66585 0C8.87342 0 10.0489 0.388613 11.0186 1.10837C11.9882 1.82813 12.7004 2.84082 13.05 3.99669C13.3996 5.15256 13.3679 6.39024 12.9596 7.52671C12.5514 8.66317 11.7882 9.63809 10.783 10.3073C12.6013 10.9774 14.1542 12.2176 15.2099 13.8426ZM23.4515 13.8285C22.3955 12.2103 20.8461 10.9756 19.033 10.3073C20.2197 9.50793 21.0572 8.28641 21.375 6.89136C21.6928 5.4963 21.467 4.03258 20.7436 2.79812C20.0202 1.56366 18.8536 0.651256 17.4812 0.246622C16.1089 -0.158011 14.6339 -0.024459 13.3565 0.620095C13.3076 0.645315 13.2649 0.680966 13.2314 0.724522C13.1978 0.768079 13.1743 0.818476 13.1624 0.872146C13.1505 0.925815 13.1506 0.981443 13.1625 1.03509C13.1745 1.08874 13.1982 1.1391 13.2318 1.18259C14.1816 2.36742 14.7271 3.82526 14.7884 5.34258C14.8496 6.8599 14.4234 8.35695 13.5721 9.61447C13.5171 9.69665 13.4967 9.79724 13.5155 9.89434C13.5343 9.99144 13.5907 10.0772 13.6724 10.1329C14.7823 10.9075 15.7325 11.8889 16.4708 13.0232C16.7686 13.4793 16.8903 14.0281 16.813 14.5673C16.8043 14.6209 16.8074 14.6758 16.822 14.7281C16.8366 14.7805 16.8624 14.829 16.8977 14.8704C16.9329 14.9117 16.9767 14.945 17.026 14.9677C17.0753 14.9905 17.129 15.0023 17.1833 15.0023H22.8365C23.0016 15.0023 23.1622 14.9479 23.2932 14.8474C23.4242 14.7468 23.5184 14.6059 23.5612 14.4463C23.5872 14.3414 23.5909 14.2322 23.572 14.1258C23.5531 14.0193 23.5121 13.9181 23.4515 13.8285Z"
                  fill="#BC7AFF"
                />
              </g>
            </svg>
            <span class="community-card__section-name">Meltano Community</span>
            <span class="community-card__badge community-card__badge--current">CURRENT</span>
          </div>
          <p class="community-card__section-desc">
            {{ label }} connector is available on Meltano Community. It is built by our growing
            community of over 5000+ developers. Refer to the Install section below to verify the
            readiness of this connector.
          </p>
          <ul class="community-card__perks">
            <li>
              <svg
                class="community-card__check-icon"
                viewBox="0 0 20 20"
                fill="none"
                aria-hidden="true"
              >
                <g transform="translate(1.875, 1.875)">
                  <path
                    d="M8.125 0C6.51803 0 4.94714 0.476523 3.611 1.36931C2.27485 2.2621 1.23344 3.53105 0.618482 5.0157C0.00352043 6.50035 -0.157382 8.13401 0.156123 9.71011C0.469628 11.2862 1.24346 12.7339 2.37976 13.8702C3.51606 15.0065 4.9638 15.7804 6.53989 16.0939C8.11599 16.4074 9.74966 16.2465 11.2343 15.6315C12.719 15.0166 13.9879 13.9752 14.8807 12.639C15.7735 11.3029 16.25 9.73197 16.25 8.125C16.2477 5.97081 15.391 3.90551 13.8677 2.38227C12.3445 0.85903 10.2792 0.00227486 8.125 0ZM11.6922 6.69219L7.31719 11.0672C7.25915 11.1253 7.19022 11.1714 7.11434 11.2029C7.03847 11.2343 6.95714 11.2505 6.875 11.2505C6.79287 11.2505 6.71154 11.2343 6.63567 11.2029C6.55979 11.1714 6.49086 11.1253 6.43282 11.0672L4.55782 9.19219C4.44054 9.07491 4.37466 8.91585 4.37466 8.75C4.37466 8.58415 4.44054 8.42509 4.55782 8.30781C4.67509 8.19054 4.83415 8.12465 5 8.12465C5.16586 8.12465 5.32492 8.19054 5.44219 8.30781L6.875 9.74141L10.8078 5.80781C10.8659 5.74974 10.9348 5.70368 11.0107 5.67225C11.0866 5.64083 11.1679 5.62465 11.25 5.62465C11.3321 5.62465 11.4134 5.64083 11.4893 5.67225C11.5652 5.70368 11.6341 5.74974 11.6922 5.80781C11.7503 5.86588 11.7963 5.93482 11.8277 6.01069C11.8592 6.08656 11.8754 6.16788 11.8754 6.25C11.8754 6.33212 11.8592 6.41344 11.8277 6.48931C11.7963 6.56518 11.7503 6.63412 11.6922 6.69219Z"
                    fill="#B7B7B7"
                  />
                </g>
              </svg>
              <span>Open source</span>
            </li>
            <li>
              <svg
                class="community-card__check-icon"
                viewBox="0 0 20 20"
                fill="none"
                aria-hidden="true"
              >
                <g transform="translate(1.875, 1.875)">
                  <path
                    d="M8.125 0C6.51803 0 4.94714 0.476523 3.611 1.36931C2.27485 2.2621 1.23344 3.53105 0.618482 5.0157C0.00352043 6.50035 -0.157382 8.13401 0.156123 9.71011C0.469628 11.2862 1.24346 12.7339 2.37976 13.8702C3.51606 15.0065 4.9638 15.7804 6.53989 16.0939C8.11599 16.4074 9.74966 16.2465 11.2343 15.6315C12.719 15.0166 13.9879 13.9752 14.8807 12.639C15.7735 11.3029 16.25 9.73197 16.25 8.125C16.2477 5.97081 15.391 3.90551 13.8677 2.38227C12.3445 0.85903 10.2792 0.00227486 8.125 0ZM11.6922 6.69219L7.31719 11.0672C7.25915 11.1253 7.19022 11.1714 7.11434 11.2029C7.03847 11.2343 6.95714 11.2505 6.875 11.2505C6.79287 11.2505 6.71154 11.2343 6.63567 11.2029C6.55979 11.1714 6.49086 11.1253 6.43282 11.0672L4.55782 9.19219C4.44054 9.07491 4.37466 8.91585 4.37466 8.75C4.37466 8.58415 4.44054 8.42509 4.55782 8.30781C4.67509 8.19054 4.83415 8.12465 5 8.12465C5.16586 8.12465 5.32492 8.19054 5.44219 8.30781L6.875 9.74141L10.8078 5.80781C10.8659 5.74974 10.9348 5.70368 11.0107 5.67225C11.0866 5.64083 11.1679 5.62465 11.25 5.62465C11.3321 5.62465 11.4134 5.64083 11.4893 5.67225C11.5652 5.70368 11.6341 5.74974 11.6922 5.80781C11.7503 5.86588 11.7963 5.93482 11.8277 6.01069C11.8592 6.08656 11.8754 6.16788 11.8754 6.25C11.8754 6.33212 11.8592 6.41344 11.8277 6.48931C11.7963 6.56518 11.7503 6.63412 11.6922 6.69219Z"
                    fill="#B7B7B7"
                  />
                </g>
              </svg>
              <span>Access to Slack community</span>
            </li>
          </ul>
        </div>

        <div class="community-card__divider"></div>

        <!-- Meltano Cloud section -->
        <div class="community-card__section">
          <div class="community-card__title-row">
            <svg
              class="community-card__section-icon"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
            >
              <g transform="translate(3, 3.75)">
                <path
                  d="M16.5 0H1.5C1.10218 0 0.720644 0.158035 0.43934 0.43934C0.158035 0.720644 0 1.10218 0 1.5V6.75C0 11.6925 2.3925 14.6878 4.39969 16.3303C6.56156 18.0984 8.71219 18.6984 8.80594 18.7238C8.93485 18.7588 9.07078 18.7588 9.19969 18.7238C9.29344 18.6984 11.4413 18.0984 13.6059 16.3303C15.6075 14.6878 18 11.6925 18 6.75V1.5C18 1.10218 17.842 0.720644 17.5607 0.43934C17.2794 0.158035 16.8978 0 16.5 0ZM13.2825 6.53063L8.0325 11.7806C7.96285 11.8504 7.88013 11.9057 7.78908 11.9434C7.69803 11.9812 7.60044 12.0006 7.50187 12.0006C7.40331 12.0006 7.30572 11.9812 7.21467 11.9434C7.12362 11.9057 7.0409 11.8504 6.97125 11.7806L4.72125 9.53063C4.58052 9.38989 4.50146 9.19902 4.50146 9C4.50146 8.80098 4.58052 8.61011 4.72125 8.46937C4.86198 8.32864 5.05285 8.24958 5.25187 8.24958C5.4509 8.24958 5.64177 8.32864 5.7825 8.46937L7.5 10.1897L12.2194 5.46937C12.2891 5.39969 12.3718 5.34442 12.4628 5.3067C12.5539 5.26899 12.6515 5.24958 12.75 5.24958C12.8485 5.24958 12.9461 5.26899 13.0372 5.3067C13.1282 5.34442 13.2109 5.39969 13.2806 5.46937C13.3503 5.53906 13.4056 5.62178 13.4433 5.71283C13.481 5.80387 13.5004 5.90145 13.5004 6C13.5004 6.09855 13.481 6.19613 13.4433 6.28717C13.4056 6.37822 13.3503 6.46094 13.2806 6.53063H13.2825Z"
                  fill="#3A64FA"
                />
              </g>
            </svg>
            <span class="community-card__section-name">Meltano Cloud</span>
            <span class="community-card__badge community-card__badge--new">NEW</span>
          </div>
          <p class="community-card__section-desc">
            For teams that want an easy, managed setup and personalised expert support,
            <a href="https://meltano.com/connectors?tab=cloud" target="_blank" rel="noopener noreferrer"
              >explore Meltano Cloud
            </a>
          </p>
          <ul class="community-card__perks community-card__perks--cloud">
            <li>
              <svg
                class="community-card__check-icon"
                viewBox="0 0 20 20"
                fill="none"
                aria-hidden="true"
              >
                <g transform="translate(1.875, 1.875)">
                  <path
                    d="M8.125 0C6.51803 0 4.94714 0.476523 3.611 1.36931C2.27485 2.2621 1.23344 3.53105 0.618482 5.0157C0.00352043 6.50035 -0.157382 8.13401 0.156123 9.71011C0.469628 11.2862 1.24346 12.7339 2.37976 13.8702C3.51606 15.0065 4.9638 15.7804 6.53989 16.0939C8.11599 16.4074 9.74966 16.2465 11.2343 15.6315C12.719 15.0166 13.9879 13.9752 14.8807 12.639C15.7735 11.3029 16.25 9.73197 16.25 8.125C16.2477 5.97081 15.391 3.90551 13.8677 2.38227C12.3445 0.85903 10.2792 0.00227486 8.125 0ZM11.6922 6.69219L7.31719 11.0672C7.25915 11.1253 7.19022 11.1714 7.11434 11.2029C7.03847 11.2343 6.95714 11.2505 6.875 11.2505C6.79287 11.2505 6.71154 11.2343 6.63567 11.2029C6.55979 11.1714 6.49086 11.1253 6.43282 11.0672L4.55782 9.19219C4.44054 9.07491 4.37466 8.91585 4.37466 8.75C4.37466 8.58415 4.44054 8.42509 4.55782 8.30781C4.67509 8.19054 4.83415 8.12465 5 8.12465C5.16586 8.12465 5.32492 8.19054 5.44219 8.30781L6.875 9.74141L10.8078 5.80781C10.8659 5.74974 10.9348 5.70368 11.0107 5.67225C11.0866 5.64083 11.1679 5.62465 11.25 5.62465C11.3321 5.62465 11.4134 5.64083 11.4893 5.67225C11.5652 5.70368 11.6341 5.74974 11.6922 5.80781C11.7503 5.86588 11.7963 5.93482 11.8277 6.01069C11.8592 6.08656 11.8754 6.16788 11.8754 6.25C11.8754 6.33212 11.8592 6.41344 11.8277 6.48931C11.7963 6.56518 11.7503 6.63412 11.6922 6.69219Z"
                    fill="#BC7AFF"
                  />
                </g>
              </svg>
              <span>No maintenance overhead</span>
            </li>
            <li>
              <svg
                class="community-card__check-icon"
                viewBox="0 0 20 20"
                fill="none"
                aria-hidden="true"
              >
                <g transform="translate(1.875, 1.875)">
                  <path
                    d="M8.125 0C6.51803 0 4.94714 0.476523 3.611 1.36931C2.27485 2.2621 1.23344 3.53105 0.618482 5.0157C0.00352043 6.50035 -0.157382 8.13401 0.156123 9.71011C0.469628 11.2862 1.24346 12.7339 2.37976 13.8702C3.51606 15.0065 4.9638 15.7804 6.53989 16.0939C8.11599 16.4074 9.74966 16.2465 11.2343 15.6315C12.719 15.0166 13.9879 13.9752 14.8807 12.639C15.7735 11.3029 16.25 9.73197 16.25 8.125C16.2477 5.97081 15.391 3.90551 13.8677 2.38227C12.3445 0.85903 10.2792 0.00227486 8.125 0ZM11.6922 6.69219L7.31719 11.0672C7.25915 11.1253 7.19022 11.1714 7.11434 11.2029C7.03847 11.2343 6.95714 11.2505 6.875 11.2505C6.79287 11.2505 6.71154 11.2343 6.63567 11.2029C6.55979 11.1714 6.49086 11.1253 6.43282 11.0672L4.55782 9.19219C4.44054 9.07491 4.37466 8.91585 4.37466 8.75C4.37466 8.58415 4.44054 8.42509 4.55782 8.30781C4.67509 8.19054 4.83415 8.12465 5 8.12465C5.16586 8.12465 5.32492 8.19054 5.44219 8.30781L6.875 9.74141L10.8078 5.80781C10.8659 5.74974 10.9348 5.70368 11.0107 5.67225C11.0866 5.64083 11.1679 5.62465 11.25 5.62465C11.3321 5.62465 11.4134 5.64083 11.4893 5.67225C11.5652 5.70368 11.6341 5.74974 11.6922 5.80781C11.7503 5.86588 11.7963 5.93482 11.8277 6.01069C11.8592 6.08656 11.8754 6.16788 11.8754 6.25C11.8754 6.33212 11.8592 6.41344 11.8277 6.48931C11.7963 6.56518 11.7503 6.63412 11.6922 6.69219Z"
                    fill="#BC7AFF"
                  />
                </g>
              </svg>
              <span>Rigorously tested</span>
            </li>
            <li>
              <svg
                class="community-card__check-icon"
                viewBox="0 0 20 20"
                fill="none"
                aria-hidden="true"
              >
                <g transform="translate(1.875, 1.875)">
                  <path
                    d="M8.125 0C6.51803 0 4.94714 0.476523 3.611 1.36931C2.27485 2.2621 1.23344 3.53105 0.618482 5.0157C0.00352043 6.50035 -0.157382 8.13401 0.156123 9.71011C0.469628 11.2862 1.24346 12.7339 2.37976 13.8702C3.51606 15.0065 4.9638 15.7804 6.53989 16.0939C8.11599 16.4074 9.74966 16.2465 11.2343 15.6315C12.719 15.0166 13.9879 13.9752 14.8807 12.639C15.7735 11.3029 16.25 9.73197 16.25 8.125C16.2477 5.97081 15.391 3.90551 13.8677 2.38227C12.3445 0.85903 10.2792 0.00227486 8.125 0ZM11.6922 6.69219L7.31719 11.0672C7.25915 11.1253 7.19022 11.1714 7.11434 11.2029C7.03847 11.2343 6.95714 11.2505 6.875 11.2505C6.79287 11.2505 6.71154 11.2343 6.63567 11.2029C6.55979 11.1714 6.49086 11.1253 6.43282 11.0672L4.55782 9.19219C4.44054 9.07491 4.37466 8.91585 4.37466 8.75C4.37466 8.58415 4.44054 8.42509 4.55782 8.30781C4.67509 8.19054 4.83415 8.12465 5 8.12465C5.16586 8.12465 5.32492 8.19054 5.44219 8.30781L6.875 9.74141L10.8078 5.80781C10.8659 5.74974 10.9348 5.70368 11.0107 5.67225C11.0866 5.64083 11.1679 5.62465 11.25 5.62465C11.3321 5.62465 11.4134 5.64083 11.4893 5.67225C11.5652 5.70368 11.6341 5.74974 11.6922 5.80781C11.7503 5.86588 11.7963 5.93482 11.8277 6.01069C11.8592 6.08656 11.8754 6.16788 11.8754 6.25C11.8754 6.33212 11.8592 6.41344 11.8277 6.48931C11.7963 6.56518 11.7503 6.63412 11.6922 6.69219Z"
                    fill="#BC7AFF"
                  />
                </g>
              </svg>
              <span>Expert support from Meltano</span>
            </li>
          </ul>
          <div class="community-card__actions">
            <a
              href="https://meltano.com/contact"
              target="_blank"
              rel="noopener noreferrer"
              class="community-card__btn community-card__btn--light"
            >
              Know more
            </a>
            <a
              href="https://meetings.hubspot.com/kyle-john"
              target="_blank"
              rel="noopener noreferrer"
              class="community-card__btn community-card__btn--primary"
            >
              Book a demo
            </a>
          </div>
        </div>
      </div>
      <div class="single-plugin-aside order-first lg:order-last p-5">
        <div class="px-4 aside-inner space-y-4">
          <div>
            <p class="text-lg py-2">Install</p>
            <div class="space-y-2">
              <div class="flex border-b border-gray-200">
                <button
                  @click="activeTab = 'modern'"
                  :class="[
                    'px-2 py-1 text-xs font-medium border-b-2 transition-colors',
                    activeTab === 'modern'
                      ? 'border-blue-500 text-blue-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700',
                  ]"
                >
                  v3.8+
                </button>
                <button
                  @click="activeTab = 'legacy'"
                  :class="[
                    'px-2 py-1 text-xs font-medium border-b-2 transition-colors',
                    activeTab === 'legacy'
                      ? 'border-blue-500 text-blue-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700',
                  ]"
                >
                  Legacy
                </button>
              </div>
              <div v-if="activeTab === 'legacy'">
                <code class="break-word bg-white-07 rounded p-2 text-sm"
                  >meltano add {{ plugin_type }} {{ name
                  }}<span v-if="!is_default"> --variant {{ variant }}</span></code
                >
              </div>
              <div v-if="activeTab === 'modern'">
                <code class="break-word bg-white-07 rounded p-2 text-sm"
                  >meltano add
                  <span
                    v-if="
                      plugin_type === 'extractor' ||
                      plugin_type === 'loader' ||
                      plugin_type === 'utility'
                    "
                    >{{ name }}</span
                  ><span v-else>--plugin-type {{ plugin_type }} {{ name }}</span
                  ><span v-if="!is_default"> --variant {{ variant }}</span></code
                >
              </div>
            </div>
          </div>
          <div></div>
          <div>
            <p class="text-lg">Maintenance Status</p>
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  v-if="maintenance_status === 'active'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Active%20(Stable)-brightgreen"
                />
                <img
                  v-else-if="maintenance_status === 'unknown'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Unknown-lightgrey"
                />
                <img
                  v-else-if="maintenance_status === 'development'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Development%20(Under%20Construction)-orange"
                />
                <img
                  v-else-if="maintenance_status === 'beta'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Prerelease%20(Beta)-yellow"
                />
                <img
                  v-else-if="maintenance_status === 'inactive'"
                  alt="Maintenance Status"
                  src="https://img.shields.io/badge/Maintenance%20Status-Inactive%20or%20Stale-red"
                />
              </li>
              <li v-if="(keywords ?? []).includes('meltano_sdk')">
                <a href="https://sdk.meltano.com/en/latest/">
                  <img
                    alt="Built with the Meltano SDK"
                    src="https://img.shields.io/badge/Built%20with%20the%20Meltano%20SDK-✔-blueviolet"
                  />
                </a>
              </li>
              <li v-if="(keywords ?? []).includes('airbyte_protocol')">
                <a
                  :href="`https://docs.airbyte.com/integrations/${airbyte_name.replace('-', 's/')}`"
                >
                  <img
                    alt="Based on an Airbyte Connector"
                    src="https://img.shields.io/badge/Based%20on%20an%20Airbyte%20Connector-🔗-orange"
                  />
                </a>
              </li>
            </ul>
          </div>
          <div>
            <p class="text-lg">Repo</p>
            <div>
              <img
                v-if="repo.type === 'github'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/github-brands.svg"
              /><img
                v-else-if="repo.type === 'gitlab'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/gitlab-brands.svg"
              /><img
                v-else-if="repo.type === 'bitbucket'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/bitbucket-brands.svg"
              /><img
                v-else
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/git-alt-brands.svg"
              /><a :href="repo.url"
                ><img
                  class="inline gap-x-11"
                  :alt="repo.url"
                  :src="`https://img.shields.io/static/v1?label=${repo.user}&message=${repo.name}&color=blue`"
                />
              </a>
            </div>
          </div>
          <div
            v-if="!$page.plugins.keywords.includes('airbyte_protocol') && repo.type !== 'bitbucket'"
          >
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  alt="Stars"
                  :src="`https://img.shields.io/${repo.type}/stars/${repo.user}/${repo.name}?label=Stars`"
                />
              </li>
              <li>
                <img
                  alt="Forks"
                  :src="`https://img.shields.io/${repo.type}/forks/${repo.user}/${repo.name}?label=Forks`"
                />
              </li>
              <li>
                <img
                  alt="Last Commit Date"
                  :src="`https://img.shields.io/${repo.type}/last-commit/${repo.user}/${repo.name}?label=Last%20Commit`"
                />
              </li>
              <li>
                <img
                  alt="Open Issues"
                  :src="`https://img.shields.io/${
                    repo.type === 'github' ? 'github/issues-raw' : 'gitlab/issues/open-raw'
                  }/${repo.user}/${repo.name}?label=Open%20Issues`"
                />
              </li>
              <li>
                <img
                  alt="Open PRs"
                  :src="`https://img.shields.io/${
                    repo.type === 'github' ? 'github/issues-pr-raw' : 'gitlab/merge-requests/open'
                  }/${repo.user}/${repo.name}?label=Open%20Pull%20Requests`"
                />
              </li>
              <li>
                <img
                  alt="Contributors"
                  :src="`https://img.shields.io/${repo.type}/contributors/${repo.user}/${repo.name}?label=Contributors`"
                />
              </li>
              <li>
                <img
                  alt="License"
                  :src="`https://img.shields.io/${repo.type}/license/${repo.user}/${repo.name}?color=c0c0c4&label=License`"
                />
              </li>
            </ul>
          </div>
          <div
            v-if="
              $page.plugins.pluginType === 'extractor' &&
              $page.plugins.keywords.includes('airbyte_protocol')
            "
          >
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  alt="Last Commit Date"
                  :src="
                    (() => {
                      const url = `https://img.shields.io/${repo.type}/last-commit/${repo.user}/${repo.name}?label=Last%20Commit`;
                      const [path] = repo.url.match(/airbyte-integrations\S+/) ?? [];

                      return path ? `${url}&path=${path}` : url;
                    })()
                  "
                />
              </li>
              <li>
                <img alt="License" :src="`https://img.shields.io/badge/License-MIT-lightgrey`" />
              </li>
            </ul>
          </div>
          <div v-if="ext_repo">
            <p class="text-lg">EDK Extension Repo</p>
            <div>
              <img
                v-if="repo.type === 'github'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/github-brands.svg"
              /><img
                v-else-if="repo.type === 'gitlab'"
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/gitlab-brands.svg"
              /><img
                v-else
                class="w-8 h-4 inline gap-x-11"
                src="../assets/images/git-alt-brands.svg"
              /><a :href="ext_repo"
                ><img
                  class="inline gap-x-11"
                  :alt="ext_repo"
                  :src="`https://img.shields.io/static/v1?label=${parsedEDKRepo.user}&message=${parsedEDKRepo.repo_name}&color=blue`"
                />
              </a>
            </div>
          </div>
          <div>
            <p class="text-lg">Maintainer</p>
            <ul class="list-disc list-inside shields">
              <li>
                <a v-if="maintainer" :href="maintainer.url"
                  ><img
                    :alt="maintainer.label"
                    :src="`https://img.shields.io/static/v1?label=&message=${maintainer.label}&color=grey`"
                  /> </a
                ><img
                  v-else
                  :alt="variant"
                  :src="`https://img.shields.io/static/v1?label=&message=${variant}&color=grey`"
                />
              </li>
            </ul>
          </div>
          <!-- <div v-if="metrics  (keywords ?? []).includes('meltano_sdk')"> -->
          <div v-if="metrics && (metrics.all_execs || metrics.all_projects)">
            <p class="text-lg">Meltano Stats</p>
            <ul class="list-disc list-inside shields space-y-1">
              <li v-if="metrics.all_execs">
                <img
                  alt="Total Executions (Last 3 Months)"
                  :src="`https://img.shields.io/badge/Total%20Executions%20(Last%203%20Months)-${metrics.all_execs.toLocaleString()}-c0c0c4`"
                />
              </li>
              <li v-if="metrics.all_projects">
                <img
                  alt="Projects (Last 3 Months)"
                  :src="`https://img.shields.io/badge/Projects%20(Last%203%20Months)-${metrics.all_projects.toLocaleString()}-c0c0c4`"
                />
              </li>
            </ul>
          </div>
          <div v-if="hasPyPI">
            <p class="text-lg">PyPI Stats</p>
            <ul class="list-disc list-inside shields space-y-1">
              <li>
                <img
                  alt="PyPI Downloads"
                  :src="`https://img.shields.io/pypi/dm/${pip_url}?color=3438BF&label=PyPI%20Downloads&`"
                  :href="`https://pypi.org/project/${pip_url}/`"
                />
              </li>
              <li>
                <img
                  alt="PyPI Package Version"
                  :src="`https://img.shields.io/pypi/v/${pip_url}?color=3438BF&label=PyPI%20Package%20Version&`"
                  :href="`https://pypi.org/project/${pip_url}/`"
                />
              </li>
            </ul>
          </div>
          <div>
            <p class="text-lg">Keywords</p>
            <ul class="list-disc list-inside shields">
              <li>
                <img
                  v-for="(keyword, index) in keywords"
                  v-bind:key="index"
                  class="inline mr-1"
                  :alt="keyword"
                  :src="`https://img.shields.io/static/v1?label=&message=${keyword}&color=grey`"
                />
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PluginSidebar",
  props: [
    "name",
    "label",
    "airbyte_name",
    "domain_url",
    "is_default",
    "repo",
    "maintenance_status",
    "keywords",
    "variant",
    "plugin_type",
    "metrics",
    "maintainer",
    "pip_url",
    "ext_repo",
  ],
  data() {
    return {
      activeTab: "modern",
    };
  },
  computed: {
    parsedEDKRepo() {
      // For some plugin variants, either the `variant` or `name` doesn't match the GH repo
      // So we need to parse it from the repo URL to make badges
      // https://github.com/:user/:repoName
      const urlParts = this.ext_repo.split("/");
      return { user: urlParts[3], repo_name: urlParts[4] };
    },
    repoEDKType() {
      // Some plugins are hosted on github, some on gitlab
      return this.ext_repo.includes("github.com") ? "github" : "gitlab";
    },
    hasPyPI() {
      // Exclude more elaborate ways of specifying `pip_url`
      // TODO: figure out what we should do when
      //   - multiple packages are listed space-delimited
      //   - packages have version specifiers (==, ~=)
      //   - packages specify optional dependencies in []
      return (
        this.pip_url &&
        !(
          this.pip_url.includes("git+") ||
          this.pip_url.includes("//") ||
          this.pip_url.includes("=") ||
          this.pip_url.includes(" ") ||
          this.pip_url.includes("[")
        )
      );
    },
  },
};
</script>

<style lang="scss">
.shields {
  list-style-type: none;
  padding: 0 0 0 30px;
}

.community-card {
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding: 33px;
  margin-bottom: 16px;
  border-radius: 8px;
  background: #f4f1ff;
  border: 1px solid rgba(49, 23, 114, 0.15);

  &__section {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  &__title-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  &__section-icon {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
  }

  &__section-name {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1d2939;
    font-family: "Inter", sans-serif;
    letter-spacing: -0.025em;
    line-height: 1.2;
    white-space: nowrap;
  }

  &__badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    font-family: "Plus Jakarta Sans", sans-serif;
    line-height: normal;
    white-space: nowrap;

    &--current {
      background: #e4e4e4;
      color: #1d2939;
    }

    &--new {
      background: #7c7aff;
      color: #ffffff;
    }
  }

  &__section-desc {
    font-size: 0.875rem;
    color: #1d2939;
    line-height: 1.2;
    margin: 0;
    font-family: "Inter", sans-serif;
    letter-spacing: -0.02em;
  }

  &__divider {
    height: 1px;
    background: #d0d5dd;
    width: 100%;
    flex-shrink: 0;
  }

  &__perks {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;

    li {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 1rem;
      font-weight: 600;
      color: #1d2939;
      font-family: "Plus Jakarta Sans", sans-serif;
      line-height: normal;
    }
  }

  &__check-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
  }

  &__actions {
    display: flex;
    gap: 16px;
  }

  &__btn {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1;
    height: 44px;
    padding: 12px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    font-family: "Plus Jakarta Sans", sans-serif;
    text-align: center;
    transition: opacity 0.15s ease;

    &:hover {
      opacity: 0.9;
      text-decoration: none;
    }

    &--light {
      background: #ffffff;
      color: #1d2939 !important;
    }

    &--primary {
      background: #3a64fa;
      color: #ffffff !important;
    }
  }
}
</style>
