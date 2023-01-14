import React, { Component } from 'react'
import PostData from '../data/posts.json'

import PostDetail from './PostDetail'
class PostList extends Component {
  render () {
    return (

      <div>
        {PostData.map((item, index) => {
          return <PostDetail post={item} key={'post-list-key ${index}'}/>
        })}
      </div>

    )
  }
}

export default PostList
