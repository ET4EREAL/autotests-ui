from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage
from elements.button import Button
from elements.text import Text


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Заголовок и кнопка создания курса
        self.courses_title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Create course')

        # Меню курса
        self.course_menu_button = Button(page, 'course-view-menu-button', 'Menu')
        self.course_edit_menu_item = Button(page, 'course-view-edit-menu-item', 'Edit')
        self.course_delete_menu_item = Button(page, 'course-view-delete-menu-item', 'Delete')

    def check_visible_courses_title(self):
        self.courses_title.check_visible()
        self.courses_title.check_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def click_edit(self):
        self.course_menu_button.click()
        self.course_edit_menu_item.click()