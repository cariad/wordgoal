from pytest import mark

from wordgoal.document_types import DocumentType, get_document_type


@mark.parametrize(
    "suffix, expect",
    [
        ("", DocumentType.UNHANDLED),
        (".foo", DocumentType.UNHANDLED),
        (".markdown", DocumentType.MARKDOWN),
        (".md", DocumentType.MARKDOWN),
        (".text", DocumentType.TEXT),
        (".txt", DocumentType.TEXT),
    ],
)
def test_get_document_type(suffix: str, expect: DocumentType) -> None:
    assert get_document_type(suffix) == expect
    assert get_document_type(suffix.upper()) == expect
    assert get_document_type(suffix.lower()) == expect
