import React, { Component } from "react";
import { ActivityIndicator, FlatList, Text, View, StyleSheet,Image } from "react-native";
import { List, ListItem } from "react-native-elements";

export default class App extends Component {
  state = {
    data: [],
    page: 0,
    loading: false
  };

  componentWillMount() {
    this.fetchData();
  }
  componentDidUpdate(prevProps) {
    // Typical usage (don't forget to compare props):
    if (this.props.data !== prevProps.data) {
      this.fetchData();
    }
  
  }
  fetchData = async () => {
    this.setState({ loading: true });
    const response = await fetch(
      `https://randomuser.me/api?results=15&seed=hi&page=${this.state.page}`
    );
    const json = await response.json();
    this.setState(state => ({
      data: [...state.data, ...json.results],
      loading: false
    }));
  };

  handleEnd = () => {
    console.log('1111')
    this.setState(state => ({ page: state.page + 1 }), () => this.fetchData());
  };

  render() {
    return (
      <View style={styles.container}>
        <FlatList
          data={this.state.data}
          horizontal={false}
          numColumns={2}
          keyExtractor={(x, i) => i}
          onEndReached={() => this.handleEnd()}
          onEndReachedThreshold={Platform.OS == 'ios' ? 0.5 : 0.4}
          renderItem={({ item }) =>
            <Card 
              uri={item.picture.medium} key={item.name.title} name={item.name.first}
            />
          }
        />
      </View>
    );
  }
}


const Card = props => {
  return (<View style={styles.card}>
      <Image style={styles.image} source={{ uri: props.uri }} />
      <Text style={styles.text}>{props.name}</Text>
  </View>)
}
const styles = StyleSheet.create({
  container: {
      flex:1,
      justifyContent:'space-between'
  },
  card: {
      flexDirection: 'column',
      alignItems:'center',
      justifyContent:'center',
      paddingLeft:5
  },
  image: {
      width: 200,
      height: 200
  },
  text:{
     paddingTop:3,
     fontSize:15
  }
});