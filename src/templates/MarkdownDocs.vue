<template>
  <Layout>
    <div class="grid w-full">
      <div class="h-7 max-h-7"></div>
      <div class=" bg-white border text-black w-full prose lg:prose-xl" v-html="$page.markdown.content"/>
      <div class="h-7 max-h-7"></div>
    </div>
  </Layout>
</template>

<page-query lang="graphql">
query MarkdownDocs($id: ID!) {
  markdown: markdownDocs (id: $id) {
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
