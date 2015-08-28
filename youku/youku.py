#coding=utf-8
#author: wwj718
#author_email: wuwenjie718@gmail.com
#author_blog: wwj718.github.io

""" youkuXBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment

class youkuXBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="youku player",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")


    app_id = String(display_name="video client_id",
	default="youku",
	scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
	help="The  client_id for your video.")

    file_id = String(display_name="video vid",
	default="youku",
	scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
	help="The vid for your video.")


    width = Integer(display_name="Video player width",
	default="560",
	scope=Scope.content,
	help="The width for your video player.")
    height = Integer(display_name="Video player height",
	default="320",
	scope=Scope.content,
	help="The height for your video player.")

    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        '''
	    #添加字段记录上回播放时间，应该是用户级别的
	    if self.start_time != "" and self.end_time != "":
            fullUrl += "#t=" + self.start_time + "," + self.end_time
        elif self.start_time != "":
            fullUrl += "#t=" + self.start_time
        elif self.end_time != "":
            fullUrl += "#t=0," + self.end_time
        '''
        context = {
            'display_name': self.display_name,
            'app_id' : self.app_id,
            'file_id': self.file_id,
            'width': self.width,
            'height': self.height
        }
        html = self.render_template('static/html/youku_view.html', context)
        frag = Fragment(html)
        #frag.add_javascript(self.load_resource('static/js/h5connect.js')) #内有中文，使用插入外部url
        frag.add_javascript(self.load_resource("static/js/youku_api.js"))
        frag.add_javascript(self.load_resource("static/js/youku_view.js"))
        frag.initialize_js('youkuXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'app_id' : self.app_id,
            'file_id': self.file_id,
            'width': self.width,
            'height': self.height
        }
        html = self.render_template('static/html/youku_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/youku_edit.js"))
        frag.initialize_js('youkuXBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_youku(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.app_id = data['app_id']
        self.file_id = data['file_id']
        self.width = data['width']
        self.height = data['height']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def get_params(self, data, suffix=''):
        '''called when youku init'''
        return {"file_id":self.file_id,
                "app_id":self.app_id,
                "width":self.width,
                "height":self.height
                }

    @staticmethod
    def workbench_scenarios():
        return [
              ("youku demo", "<youku />")  #the name should be "<youku />"
        ]
