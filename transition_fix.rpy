# 文件名: transition_fix.rpy
# 功能: 让立绘差分过渡不影响对话框的显示效果
# 作者: irigaS
# 版本: 1.0
# 说明: 此文件用于修复Ren'Py中角色立绘切换时的转场效果会影响到对话框的问题
#       通过将对话框和立绘分别放在不同的层中，确保转场效果只应用于立绘层

init python:
    class TransitionFixer:
        """
        转场修复器类
        用于管理转场效果，确保立绘切换时的转场不会影响到对话框
        """
        
        @staticmethod
        def setup():
            """
            初始化设置
            配置对话层和转场回调
            """
            # 设置对话层为screens，这样对话框就不会受到转场影响
            config.say_layer = "screens"
            
            # 设置转场回调函数
            config.with_callback = TransitionFixer.with_callback
            
            # 保存原始的with_statement函数
            TransitionFixer.original_with_statement = renpy.exports.with_statement
            
            # 替换为新的with_statement函数
            renpy.exports.with_statement = TransitionFixer.new_with_statement
        
        @staticmethod
        def with_callback(trans, paired):
            """
            转场回调函数
            确保转场效果只应用于master层
            
            Args:
                trans: 转场对象
                paired: 配对对象
            """
            if trans is None:
                return None
                
            if isinstance(trans, dict):
                return trans
                
            # 将转场限制在master层
            return { "master": trans }
        
        @staticmethod
        def handle_transition(trans, old_widget, new_widget):
            """
            处理转场对象
            
            Args:
                trans: 转场对象
                old_widget: 旧部件
                new_widget: 新部件
            """
            if isinstance(trans, dict):
                return { k: TransitionFixer.handle_transition(v, old_widget, new_widget) 
                        for k, v in trans.items() }
            elif callable(trans):
                return trans(old_widget=old_widget, new_widget=new_widget)
            return trans
        
        @staticmethod
        def new_with_statement(trans, always=False, paired=None, clear=True):
            """
            新的with_statement函数
            确保转场效果只应用于master层
            
            Args:
                trans: 转场对象
                always: 是否总是应用转场
                paired: 配对对象
                clear: 是否清除
            """
            if trans is None:
                return TransitionFixer.original_with_statement(trans, always, paired, clear)
                
            if isinstance(trans, dict):
                return TransitionFixer.original_with_statement(trans, always, paired, clear)
                
            return TransitionFixer.original_with_statement(
                { "master": trans }, always, paired, clear)

    # 初始化转场修复器
    TransitionFixer.setup()