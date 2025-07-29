from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.any_patch_item_type_0 import AnyPATCHItemType0
from ...models.any_patch_item_type_1 import AnyPATCHItemType1
from ...models.any_patch_item_type_2 import AnyPATCHItemType2
from ...models.credential_v4_credmgr_get import CredentialV4CredmgrGET
from ...types import Response


def _get_kwargs(
    spec_name: str,
    *,
    body: list[Union["AnyPATCHItemType0", "AnyPATCHItemType1", "AnyPATCHItemType2"]],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/nexus/infra/api/credmgr/v4/credentials/{spec_name}",
    }

    _kwargs["json"] = []
    for componentsschemas_any_patch_item_data in body:
        componentsschemas_any_patch_item: dict[str, Any]
        if isinstance(componentsschemas_any_patch_item_data, AnyPATCHItemType0):
            componentsschemas_any_patch_item = componentsschemas_any_patch_item_data.to_dict()
        elif isinstance(componentsschemas_any_patch_item_data, AnyPATCHItemType1):
            componentsschemas_any_patch_item = componentsschemas_any_patch_item_data.to_dict()
        else:
            componentsschemas_any_patch_item = componentsschemas_any_patch_item_data.to_dict()

        _kwargs["json"].append(componentsschemas_any_patch_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CredentialV4CredmgrGET]]:
    if response.status_code == 200:
        response_200 = CredentialV4CredmgrGET.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CredentialV4CredmgrGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["AnyPATCHItemType0", "AnyPATCHItemType1", "AnyPATCHItemType2"]],
) -> Response[Union[Any, CredentialV4CredmgrGET]]:
    """Modify an existing object of type Credential

    Args:
        spec_name (str):
        body (list[Union['AnyPATCHItemType0', 'AnyPATCHItemType1', 'AnyPATCHItemType2']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CredentialV4CredmgrGET]]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["AnyPATCHItemType0", "AnyPATCHItemType1", "AnyPATCHItemType2"]],
) -> Optional[Union[Any, CredentialV4CredmgrGET]]:
    """Modify an existing object of type Credential

    Args:
        spec_name (str):
        body (list[Union['AnyPATCHItemType0', 'AnyPATCHItemType1', 'AnyPATCHItemType2']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CredentialV4CredmgrGET]
    """

    return sync_detailed(
        spec_name=spec_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["AnyPATCHItemType0", "AnyPATCHItemType1", "AnyPATCHItemType2"]],
) -> Response[Union[Any, CredentialV4CredmgrGET]]:
    """Modify an existing object of type Credential

    Args:
        spec_name (str):
        body (list[Union['AnyPATCHItemType0', 'AnyPATCHItemType1', 'AnyPATCHItemType2']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CredentialV4CredmgrGET]]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["AnyPATCHItemType0", "AnyPATCHItemType1", "AnyPATCHItemType2"]],
) -> Optional[Union[Any, CredentialV4CredmgrGET]]:
    """Modify an existing object of type Credential

    Args:
        spec_name (str):
        body (list[Union['AnyPATCHItemType0', 'AnyPATCHItemType1', 'AnyPATCHItemType2']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CredentialV4CredmgrGET]
    """

    return (
        await asyncio_detailed(
            spec_name=spec_name,
            client=client,
            body=body,
        )
    ).parsed
