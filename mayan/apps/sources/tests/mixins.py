from __future__ import unicode_literals

from ..literals import SOURCE_CHOICE_WEB_FORM, SOURCE_UNCOMPRESS_CHOICE_Y
from ..models.watch_folder_sources import WatchFolderSource
from ..models.webform_sources import WebFormSource

from .literals import TEST_SOURCE_LABEL, TEST_SOURCE_UNCOMPRESS_N


class SourceTestMixin(object):
    auto_create_test_source = True

    def setUp(self):
        super(SourceTestMixin, self).setUp()
        if self.auto_create_test_source:
            self._create_test_source()

    def _create_test_source(self):
        self.test_source = WebFormSource.objects.create(
            enabled=True, label=TEST_SOURCE_LABEL,
            uncompress=TEST_SOURCE_UNCOMPRESS_N
        )


class SourceViewTestMixin(object):
    def _request_setup_source_list_view(self):
        return self.get(viewname='sources:setup_source_list')

    def _request_setup_source_create_view(self):
        return self.post(
            kwargs={'source_type': SOURCE_CHOICE_WEB_FORM},
            viewname='sources:setup_source_create', data={
                'enabled': True, 'label': TEST_SOURCE_LABEL,
                'uncompress': TEST_SOURCE_UNCOMPRESS_N
            }
        )

    def _request_setup_source_delete_view(self):
        return self.post(
            viewname='sources:setup_source_delete',
            kwargs={'pk': self.test_source.pk}
        )


class WatchFolderTestMixin(object):
    def _create_test_watchfolder(self):
        self.test_watch_folder = WatchFolderSource.objects.create(
            document_type=self.test_document_type,
            folder_path=self.temporary_directory,
            include_subdirectories=False,
            uncompress=SOURCE_UNCOMPRESS_CHOICE_Y
        )
