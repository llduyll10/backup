import { createSwitchNavigator } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import HomeScreen from './src/screen/Home'
import SigninScreen from './src/screen/Signin'
const AppStack = createStackNavigator({
    Home:{
        screen:{
            HomeScreen
        }
    }
})
const AuthStack = createStackNavigator({
    Auth:{
        screen:SigninScreen
    }
})

const AppNavigator = createSwitchNavigator(
    {
        App:AppStack,
        Auth:AuthStack
    },
    // {
    //     initialRouteName:'App'
    // }
)
export default AppNavigator





// import { createStackNavigator } from 'react-navigation-stack';
// import { createBottomTabNavigator } from 'react-navigation-tabs';

// import LoginScreen from './src/screen/Login'
// import SigninScreen from './src/screen/Signin'

// const LoginStack = createStackNavigator({
//     Login:{
//         screen: LoginScreen
//     }
// })
// const SigninStack = createStackNavigator({
//     Signin:{
//         screen:SigninScreen
//     }
// })

// const AppNavigator = createBottomTabNavigator({
//     Login: LoginStack,
// })

// export default AppNavigator