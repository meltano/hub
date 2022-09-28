<template>
  <Layout>
    <div class="flex w-full flex-col items-center">
      <div
        class="prose my-7 mx-10 max-w-screen-lg rounded-lg border bg-white p-4 text-black"
        v-html="$page.markdown.content"
      />
    </div>
  </Layout>
</template>

<page-query lang="graphql">
query MarkdownDocs($id: ID!) {
  markdown: markdownDocs(id: $id) {
    id
    path
    description
    title
    content
    fileInfo {
      directory
      extension
      path
      name
    }
  }
}
</page-query>
