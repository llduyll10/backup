import React,{Component} from 'react'
import { View, Text,StyleSheet} from 'react-native';

export default class NoAuth extends Component{
    render(){
        return(
            <View style={styles.container}>
                <Text style={styles.item}>Vui lòng đăng nhập để tiếp tục</Text>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container:{
        flex:1,
        marginTop:10,
        justifyContent:'center',
        alignItems:'center'
    },
    item:{
        
       
    }
})